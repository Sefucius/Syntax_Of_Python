lst=['hello','world','phthon','php']

# 使用for循环遍历列表
for  item in lst:
    print(item)
print('-----------------')

# 使用for循环，range()函数，len()函数，根据索引遍历列表
for i in range(0,len(lst)):
    print(i,'--->',lst[i])
print('-----------------')

# 使用enumerate()函数，遍历列表
for index,item in enumerate(lst):
    print(index,'--->',item) #index是序号，不是索引
print('-----------------')

#  手动修改序号的起始值
for index,item in enumerate(lst,start=1):
    print(index,'--->',item)   
print('-----------------')

for index,item in enumerate(lst,1):# 也可以省略start
    print(index,'--->',item)   
print('-----------------') 

for i,j in enumerate(lst,start=1):# 可以把index和item换掉
    print(i,'--->',j)   