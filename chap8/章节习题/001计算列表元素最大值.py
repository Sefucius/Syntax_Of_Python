# 随机生成10个整数
import random
def fun(n):
    lst=[]
    for i in range(n):
        lst.append(random.randint(1,100))
    temp=lst[0]
    for i in range(len(lst)):
        if lst[i]>temp:
            temp=lst[i]
    return lst,temp
result=fun(10)
print(result[0])
print(result[1])