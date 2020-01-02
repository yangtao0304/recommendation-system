import datetime

unix_ts = 1238536800000
t1 = datetime.datetime.fromtimestamp(unix_ts/1000)
print('1238536800000转化为时间是：{}'.format(t1))
