import time
now=time.time()
print(now)

obj=time.localtime() # struct_time对象
print(obj)

obj2=time.localtime(60) # 1970年1月1日8时1分0秒
print(obj2)
print(type(obj2))
print('年份',obj2.tm_year)
print('月份',obj2.tm_mon)
print('日期',obj2.tm_mday)
print('小时',obj2.tm_hour)
print('分钟',obj2.tm_min)
print('秒',obj2.tm_sec)
print('星期几',obj2.tm_wday) # 0-6 0代表星期一
print('一年中的第几天',obj2.tm_yday) # 1-366
print(time.ctime()) # 时间数对应的易读的字符串

# 日期时间格式化
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%H:%M:%S',time.localtime()))
print('%B月份的名称',time.strftime('%B',time.localtime()))
print('%A星期的名称',time.strftime('%A',time.localtime()))

# 字符串转struct_time
print(time.strptime('2020-06-20','%Y-%m-%d')) # 必须是字符串
print(time.strptime('2020-06-20 10:10:10','%Y-%m-%d %H:%M:%S')) # 必须是字符串

time.sleep(3) # 程序休眠3秒
print('程序结束')