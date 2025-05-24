import random
# 设置随机数种子
random.seed(10)
print(random.random())  # 生成[0.0~1.0)之间的随机小数
print(random.random())
print('-'*30)
print(random.randint(1,100))  # 生成[1,100]之间的随机整数

for i in range(10):  
    print(random.randrange(1,10,3)) # 从序列 [1, 4, 7] 里随机选取一个整数，步长为3

print(random.uniform(1,100))  # 生成[1,100]之间的随机小数

lst=[i for i in range(1,11)] # 生成[1,2,3,4,5,6,7,8,9,10]
print(lst) 
print(random.choice(lst))  # 从序列里随机选取一个元素
# 随机排序
random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)