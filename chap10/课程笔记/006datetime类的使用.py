from datetime import datetime # 从datetime模块中导入datetime类
dt=datetime.now()
print('当前系统时间为:',dt)

# datetime是一个类，手动创建这个类的对象
dt2=datetime(2020,8,8,20,8)
print('dt2的数据类型',type(dt2),'dt2所表示的日期时间',dt2)
print('年:',dt2.year,'月:',dt2.month,'日:',dt2.day,'时:',dt2.hour,'分:',dt2.minute,'秒:',dt2.second)

# 比较两个datetime类型对象的大小
labor_day=datetime(2025,4,23,16,18,0)
labor_day2=datetime(2025,4,23,16,18,1)
print('labor_day是否大于labor_day2:')
print('是' if labor_day>labor_day2 else '否')

# datetime类型与字符串进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%d %H:%M:%S') # 把datetime类型转换为字符串
print('nowdt的数据类型:',type(nowdt),'nowdt所表示的数据是什么:',nowdt)
print('nowdt_str的数据类型:',type(nowdt_str),'nowdt_str所表示的数据是什么:',nowdt_str)

# 字符串转换成datetime类型
str_datetime='2025年4月23日16点8分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日%H点%M分')
print('str_datetime的数据类型:',type(str_datetime),'str_datetime所表示的数据是什么:',str_datetime)
print('dt3的数据类型:',type(dt3),'dt3所表示的数据是什么:',dt3)