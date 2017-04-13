# -*- coding: utf-8 -*-
# !/usr/bin/env python

import asyncio
import json
from random import randint
import websockets


# 一个好像能执行多次的函数
async def time(websocket, path):
    while True:
        # now = datetime.datetime.utcnow().isoformat() + 'Z'
        # await websocket.send(now)
        data = [randint(0, 10) for i in range(3)]
        json_str = json.dumps(data)
        await websocket.send(json_str)
        # await asyncio.sleep(random.random() * 3)
        await asyncio.sleep(0.01)


start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


