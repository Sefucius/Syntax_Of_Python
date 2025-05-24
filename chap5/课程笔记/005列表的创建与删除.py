lst=['hello','world',98,'100.5']
print(lst)

# 可以使用内置的函数list()来创建列表
lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2)) # 1,3,5,7,9
print(lst3)

# 列表是可变序列，对序列的操作符、运算符、函数等都适用于列表
print(lst+lst2+lst3)
print(lst*3) # 序列相乘，重复序列
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o')) # 统计o的个数
print(lst2.index('o')) # 查找o在lst2中第一次出现的位置

# 列表的删除操作
lst4=[10,20,30]
print(lst4)

# del删除列表
del lst4
#print(lst4) # 报错
