# 方法一
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i*j}', end=' ')
    print()

# 方法二
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j,'*',i,'=',i*j, sep='',end='')
        print(end=' ')
    print()