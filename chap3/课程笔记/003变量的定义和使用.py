luck_number=8 
#创建一个整形变量,并赋值为8

my_name='小明' 
#创建一个字符串变量,并赋值为'小明'

print('luck_number的数据类型是：',type(luck_number) )
#输出luck_number的数据类型

print(my_name,'的幸运数字是：',luck_number) 

# Python动态修改变量的数据类型，通过赋不同的值就可以直接修改
luck_number='北京欢迎你'
print('luck_number的数据类型是：',type(luck_number) )

#在Python中允许多个变量指向同一个值
a=b=1
print(a,b)
print(id(a),id(b), sep='\n')
# id()函数用于获取对象的内存地址