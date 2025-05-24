# 初始化变量
answer=input('今天要上课吗？(y/n)')
while answer=='y': # 条件判断
    print('好好学习，天天向上！') # 语句块
    # 改变变量
    answer=input('今天要上课吗？(y/n)')


# 求1-100的累加和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1

# while的扩展形式
while i<=100:
    sum+=i
    i+=1
else:
    print('1-100之间的累加和:',sum)
