length=eval(input('请输入长度:'))
height=eval(input('请输入高度'))

# 长方形
for i in range(1,length+1):
    for j in range(1,height+1):
        print('*',end=' ')
    print() # 空的print换行

print('-'*50)

# 直角三角形
for i in range(1,length):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

print('-'*50)

# 倒直角三角形
for i in range(1,length+1):
    for j in range(1,length-i+2):
        print('*',end=' ')
    print()

print('-'*50)

# 等腰三角形
for i in range(1,length+1):
    for j in range(1,length+1-i):
        print(' ',end=' ')
    for k in range(1,2*i):
        print('*',end=' ')
    print()

print('-'*50)