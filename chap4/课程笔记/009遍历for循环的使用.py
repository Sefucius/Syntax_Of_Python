# 遍历字符串
for i in 'hello':
    print(i)


# range()函数，Python中的内置函数，产生一个（n,m）的整数序列，包含n，不包含m
for i in range(1,11):
    # print(i)
    if i % 2 == 0:
        print(i,'是偶数')


# 计算1-10之间的累加和
sum = 0 # 定义一个变量用于存储累加和
for i in range(1,11):
    sum += i # sum = sum + i
print('1-10之间的累加和为:',sum)        


print('-----------100到999之间的水仙花数-----------')
# 水仙花数：一个三位数，其各位数字的立方和等于该数本身
# 例如：153 = 1^3 + 5^3 + 3^3
for i in range(100,1000):
    # 百位数
    bai = i // 100
    # 十位数
    shi = i // 10 % 10
    # 个位数
    ge = i % 10
    if i == bai ** 3 + shi ** 3 + ge ** 3:
        print(i)