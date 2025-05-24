s='3.14+3'
print(s,type(s))
x=eval(s) 
# 使用eval()函数去掉s这个字符串中左右的引号，并返回结果
print(x,type(x))
# 执行了加法运算
# eval函数常与input函数一起使用，用于获取用户输入的数值
age=eval(input('请输入你的年龄：'))
# 将字符串类型转成了int类型,相当于int(age)
print(age,type(age))
# 输出age的值和类型
height=eval(input('请输入你的身高：'))
print(height,type(height))
# 将字符串类型转成了float类型,相当于float(height)

hello='北京欢迎你'
print(hello,type(hello))
print(eval('hello')) # 输出了“北京欢迎你”
# print(eval('北京欢迎你')) # 会报错，‘北京欢迎你’没有定义