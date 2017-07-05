# -*- coding: utf-8 -*-

import os
import re
import time
from threading import Thread

import redis
import umsgpack

data = dict()


def check_ip(ip, data):
    if os.name == 'nt':
        output = os.popen("ping -n 1 {}".format(ip)).read()
        if re.findall("0 received|已接收 = 0", output):
            data[ip] = False
        else:
            data[ip] = True

    elif os.uname()[0] == "Linux":
        output = os.popen("ping -c 1 {}".format(ip)).read()
        if "0 received" in output:
            data[ip] = False
        else:
            data[ip] = True


def get_ip():
    with open('ip.txt', encoding="utf-8") as f:
        ips = f.read().split("\n")
        ips = [i for i in ips if i]
    return ips


if __name__ == "__main__":
    pool = redis.ConnectionPool(host="localhost", port=6379, db=1)
    db = redis.StrictRedis(connection_pool=pool, socket_timeout=1)
    ips = get_ip()
    while True:
        for ip in ips:
            thread = Thread(target=check_ip, args=(ip, data))
            thread.setDaemon(True)
            thread.start()
        result = umsgpack.packb(data)
        db.hset("ip_status", "status", result)
        time.sleep(10)
