a=100 # 全局变量

def calc(x,y):
    return a+x+y

print(a)
print(calc(10,20))
print('-'*50)

def calc2(x,y):
    a=200 # 局部变量
    return a+x+y

print(calc2(10,20))
print(a)
# 局部变量和全局变量冲突时，优先使用局部变量

print('-'*50)

def calc3(x,y):
    global s # 声明s是全局变量
    s=300 # 局部变量
    return s+x+y

print(calc3(10,20))
print(s)