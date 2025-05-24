print('非空字符串的布尔值:', bool('hello'))
print('空字符串的布尔值:', bool('')) #空字符不是空格字符串
print('空列表的布尔值:', bool([]))
print('空列表的布尔值:', bool(list()))
print('空元组的布尔值:', bool(()))
print('空元组的布尔值:', bool(tuple()))
print('空字典的布尔值:', bool({}))
print('空字典的布尔值:', bool(dict()))
print('空集合的布尔值:', bool(set()))
print('-'*30)
print('非0数值型的布尔值:', bool(123))
print('整数0的布尔值:', bool(0))
print('浮点数0的布尔值:', bool(0.0))


print('-'*30)
# 将其它类型转成字符串类型
lst=[10,20,30]
print(type(lst),lst)
lst_str=str(lst)
print(type(lst_str),lst_str)
print('-'*30)


# float和str转成int
print('-'*30)
print(int(123.3)+int('98'))
# 注意事项
""" 
print(int('123.3')) # 报错
print(int('a')) # 报错 
"""


# int和str转成float
print('-'*30)
print(float(123)+float('3.14'))

print('-'*30)
s='hello'
print(list(s))

seq=range(1,10)
print(type(seq),seq)
print(tuple(seq))
print(set(seq))
# print(dict(seq)) # 报错，字典要求传入可迭代对象，且可迭代对象中每个元素都是有且只有两个值的序列类型
print(list(seq))
print('-'*30)
