# 函数的返回值
def calc(a,b):
    c = a + b
    return c

print(calc(10,20))
print(calc(calc(10,20),30))

# 返回值可以是多个
def get_sum(sum):
    s=0 # 累加和
    odd_sum=0 # 奇数和
    even_sum=0 # 偶数和
    for i in range(1,sum+1):
        s+=i
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return s,odd_sum,even_sum

result=get_sum(10)
print(result) # (55, 25, 30)
print(type(result)) # <class 'tuple'>
print(result[0]) # 55
print(result[1]) # 25
print(result[2]) # 30

# 解包赋值
a,b,c=get_sum(10)
print(a) # 55
print(b) # 25
print(c) # 30