# 第一段代码
age=input("请输入你的年龄：")
if age>="18":
    print("你已经成年了")

# 第二段代码
i=1
while i<10:# 这里冒号用成中文的了
    print(i) # 括号用成了中文的了
    i+=1

# 第三段代码
for i in range(3):
    uname=input("请输入你的用户名：")
    pwd=input("请输入你的密码：")
    if uname=="admin" and pwd=="123456": 
        print("登录成功")
        break
        print("登录成功")
        break
    else:
        print("登录失败")
else:
    print("登录次数过多，请稍后再试")

