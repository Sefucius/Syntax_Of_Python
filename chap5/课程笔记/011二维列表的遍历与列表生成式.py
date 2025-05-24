# 创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',120,130],
    ['上海',60,70],
    ['深圳',100,39]
]
print(lst)

# 二维列表的遍历
for row in lst:
    for item in row:
        print(item,end='\t')
    print()

print('---------------------')

# 二维列表的遍历
for i in range(len(lst)):       # len(lst) = 4
    for j in range(len(lst[i])):
        print(lst[i][j],end='\t')
    print()

# 列表生成式生成一个4行5列的二维列表

lst2=[[j for j in range(5)] for i in range(4)]
lst3=[[j for i in range(5)] for j in range(4)]
print(lst2)
print(lst3)
