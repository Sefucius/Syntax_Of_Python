d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)

# 向字典中添加元素
d[1004]='张丽丽'
print(d)

# 获取字典中所有的key
keys=d.keys() 
print(keys)
print(list(keys)) 
print(tuple(keys))

# 获取字典中所有的value
values=d.values()
print(values)
print(list(values))
print(tuple(values))

# 获取字典中所有的key-value对
lst=d.items()
print(lst)
print(list(lst))

d=dict(lst)
print(d)

# 使用pop()方法删除指定的key-value对
print(d.pop(1001)) # pop()方法返回的是被删除的value
print(d)

print(d.pop(1000,'不存在'))

# 使用popitem()方法删除字典中的最后一个key-value对
print(d.popitem()) # popitem()方法返回的是被删除的key-value对
print(d)

# 清空字典中的所有元素
d.clear()
print(d)

# python中一切皆对象，每个对象都有一个布尔值
print(bool(d)) # False
print(bool({})) # False
print(bool({1001:'李梅'})) # True
print(bool({1001:'李梅',1002:'王华'})) # True