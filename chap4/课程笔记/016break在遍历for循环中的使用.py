for i in 'hello':
    if i == 'e':
        break
    print(i)

print('------------------')

for i in range(3):
    username=input('请输入用户名:') 
    password=input('请输入密码:') 
    if username=='admin' and password=='123456': 
        print('登录成功!') 
        break # 跳出循环
    else: 
        if i<2:
            print('用户名或密码错误!','您还有',2-i,'次机会') 
else:
    print('三次均输入错误！')