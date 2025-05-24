from datetime import datetime
from datetime import timedelta

# 创建两个datetime类型的对象
delta1=datetime(2025,4,1)-datetime(2024,8,20)
print('delta1的数据类型是:',type(delta1),'delta1所表示的数据是:',delta1)
print('2024年8月20日之后的第224天是:',datetime(2024,8,20)+delta1)

# 通过传入参数的方式创建一个timedelta对象
td1=timedelta(10)
print('创建一个10天的timedelta对象:',td1)
td2=timedelta(10,11)
print('创建一个10天11小时的timedelta对象:',td2)