#创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时，后面的value会覆盖前面的value

# zip()函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2) # 生成一个zip对象
print(zipobj) # <zip object at 0x00000253300B8F48>
# print(list(zipobj)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
# 使用dict()函数
d=dict(zipobj) # 生成一个字典对象
print(d) # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d=dict(cat=10,dog=20) # 左侧cat和dog是key，右侧10和20是value
print(d) # {'cat': 10, 'dog': 20}

t=(10,20,30)
print({t:10}) # t是key，10是value，注意t是一个元组，不能作为key
'''
lst=[10,20,30]
print({lst:10}) # 报错，列表是可变数据类型，不能做键
'''
# 字典属于序列
print('max',max(d)) # max dog
print('min',min(d)) # min cat
print('len',len(d)) # len 2

