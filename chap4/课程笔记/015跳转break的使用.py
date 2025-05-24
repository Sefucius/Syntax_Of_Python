sum=0 # 存储累加和
i=1 # 初始化变量
while i<11: # 循环条件
    sum+=i # 累加
    if sum>20: # 判断累加和是否大于20
        print('累加和大于20的当前数是:',i)
        break # 跳出循环
    i+=1 # 更新变量

print('----------------------')

i=0 # 统计登录的次数
while i<3: # 循环条件
    username=input('请输入用户名:') 
    password=input('请输入密码:') 
    if username=='admin' and password=='123456': 
        print('登录成功!') 
        break # 跳出循环
    else: 
        if i<2:
            print('用户名或密码错误!','您还有',2-i,'次机会') 
    i+=1 # 统计登录次数
else: # while...else...
    print('三次均输入错误！')
    