#棱形
row=eval(input('请输入行数:'))
while row % 2 == 0:
    row = eval(input('请输入奇数行数:'))
# 棱形只有奇数行才能打印出来
else:
    length = (row+1)//2
    for i in range(1, length + 1):
        for j in range(1, length + 1 - i):
            print(' ', end=' ')
        for k in range(1, 2 * i):
            print('*', end=' ')
        print()
    for i in range(1, length):
        for j in range(1, i + 1):
            print(' ', end=' ')
        for k in range(1, 2 * (length - i)):
            print('*', end=' ')
        print()
# 棱形就相当于两个等腰三角形拼起来，只不过第二个等腰三角形是倒着的

# 空心棱形
row=eval(input('请输入行数:'))
while row % 2 == 0:
    row = eval(input('请输入奇数行数:'))
# 空心棱形只有奇数行才能打印出来
else:
    length = (row+1)//2
    for i in range(1, length + 1):
        for j in range(1, length + 1 - i):
            print(' ', end=' ')
        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    for i in range(1, length):
        for j in range(1, i + 1):
            print(' ', end=' ')
        for k in range(1, 2 * (length - i)):
            if k == 1 or k == 2 * (length - i) - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

'''
下面是自己想的,不够优美
先打印空白三角形，再打印边框，再打印空白三角形，再打印边框
# 空心棱形
row=eval(input('请输入行数:'))
while row % 2 == 0:
    row = eval(input('请输入奇数行数:'))
# 空心棱形只有奇数行才能打印出来
else:
    length = (row+1)//2
    for i in range(1, length + 1):
        for j in range(1, length + 1 - i):
            print(' ', end=' ')
        print('*', end=' ')
        for k in range(1, 2 * i - 2):
            print(' ', end=' ')
        if i!=1:
            print('*', end=' ')
        print()
    for i in range(1, length):
        for j in range(1, i + 1):
            print(' ', end=' ')
        print('*', end=' ')
        for k in range(1, 2 * (length - i) - 2):
            print(' ', end=' ')
        if i!=length-1:
            print('*', end=' ')
        print()
'''