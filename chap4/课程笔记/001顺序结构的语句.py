# 赋值运算符的顺序，从右到左
a = b = c = 1 # 链式赋值
name="张三"
age=20
a,b,c,d='room' # 序列解包，字符串分配赋值
print(a)
print(b)
print(c)
print(d)

print('-'*20,'输入/输出语句也是典型的顺序结构','-'*20)
name=input('请输入你的姓名：')
age=eval(input('请输入你的年龄：'))
luck_number=eval(input('请输入你的幸运数字：'))
print('你的姓名是：',name)
print('你的年龄是：',age)
print('你的幸运数字是：',luck_number)
 
