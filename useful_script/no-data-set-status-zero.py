"""
只针对与马弗炉。 暂时的测试脚本。
逻辑： 若一段时间没有数，则设置status为零
"""

import time
import pendulum
from influxdb import InfluxDBClient

TIME_WINDOW = 5  # min


class ZeroSetter:

    def __init__(self):
        # self.influx = InfluxDBClient('10.203.96.26', 8086, 'influx', 'patac2016', 'patac_eim')
        self.influx = InfluxDBClient('localhost', 8086, 'root', 'root', 'marshall')
        pass

    def check(self):
        pass

    def set_status(self):
        json_body = [
            {
                "measurement": "Mafu_measurement",
                "tags": {
                    'check': 'yes'
                },
                "time": int(time.time())*1000000,
                "fields": {
                    'status': 0
                },

            }
        ]

        self.influx.write(json_body)

    def query(self):
        result = self.influx.query('select * from Mafu_measurement order by desc limit 10;')

        check  = list(result.get_points())[0]['check']
        time_str  = list(result.get_points())[0]['time']

        dt = pendulum.from_format(time_str, '%Y-%m-%dT%H:%M:%SZ')

        diff_sec  = dt.diff().seconds
        if diff_sec > TIME_WINDOW * 60 and check is None:
            return 'put'
        else:
            return 'pass'

    def work(self):
        # every 2 s , we query it.
        # 如果若干时间没数，就设置其为0
        # 如果有 或 是我们自己的数 就不动
        while True:
            # query
            status = self.query()

            if status == 'put':
                self.set_status()
            else:
                pass
            time.sleep(2)
        pass

    def write_test_data(self):
        # json_body = [
        #     {
        #         "measurement": "Mafu_measurement",
        #         "tags": {
        #             "eqpt_no": "sss",
        #         },
        #         "time": "2018-01-23T15:00:00Z",
        #         "fields": {
        #             "status": 1,
        #             "value": 0.64
        #         }
        #     }
        # ]
        json_body = [
            {
                "measurement": "Mafu_measurement",
                "tags": {
                    'check': 'yes'
                },
                "time": int(time.time())*1000000,
                "fields": {
                    'status': 0
                },

            }
        ]
        res = self.influx.write_points(json_body,time_precision='u')
        print(res)


if __name__ == '__main__':
    zero = ZeroSetter()
    zero.write_test_data()
    zero.work()
#