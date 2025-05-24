d={'hello':10,'world':20,'python':30}
# 访问字典中的元素
# 1.使用d[key]
print(d['hello']) 
# 2.使用d.get(key)
print(d.get('hello')) # 10

# 二者是有区别的，使用d[key]时，如果key不存在，会报错，
# 使用d.get(key)时，如果key不存在，不会报错，而是返回None
print(d.get('hello1')) # None
# print(d['hello1']) # 报错，KeyError: 'hello1'

print(d.get('hello1','不存在'))

# 遍历字典中的元素
for item in d.items(): # 遍历字典中的元素，返回的是一个元组，元组中的元素是key和value
    print(item) # ('hello', 10) ('world', 20) ('python', 30)

# 在使用for循环遍历时，分别获取key和value
for key,value in d.items(): # 遍历字典中的元素，返回的是一个元组，元组中的元素是key和value
    print(key,'----->',value) # hello 10 world 20 python 30

# 遍历字典中的元素
for item in d: # 遍历字典中的元素，返回的是key
    print(item) # ('hello', 10) ('world', 20) ('python', 30)