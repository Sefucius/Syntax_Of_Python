number=eval(input('请输入您的6位中奖号码:'))
# 使用if语句
if number==987654 : #等值判断
    print('恭喜您中奖了')
if number!=987654 :
    print('很遗憾，您没有中奖')

print('-'*20,'以上if判断的表达式,是通过比较运算符计算出来的，结果是布尔类型','-'*20)

n=98 # 赋值操作
if n%2: # 98%2=0，0的布尔值为False，所以不执行
    print(n,'是奇数')
if not n%2: # 98%2=0，非0的布尔值为True，所以执行
    print(n,'是偶数')

print('--------判断一个字符串是否是空字符串--------')

x=input('请输入一个字符串：')
if x:   # 在Python中一切皆对象，每一个对象都有一个布尔值，空字符串的布尔值为False，非空字符串的布尔值为True 
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')

print('--------表达式也可以是一个单纯的布尔型变量--------')

flag=eval(input('请输入一个布尔类型的值:True 或 False'))
if flag:
    print('flag的值是True')

if not flag:
    print('flag的值是False')


print('--------使用if语句时,如果语句块中只有一句代码，可以将语句块直接写在冒号后面--------')
a=10
b=5
if a>b: max=a # 语句块只有一句，赋最大值
print('a和b中的最大值是:',max)