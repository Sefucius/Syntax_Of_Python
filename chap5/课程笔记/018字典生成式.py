import random
d={item:random.randint(1,100) for item in range(4)}
print(d)

# 创建两个列表
lst1=[1001,1002,1003]
lst2=['cat','dog','pet']

d={key:value for key,value in zip(lst1,lst2)}
print(d)