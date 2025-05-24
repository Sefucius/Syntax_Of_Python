#方法一
num=input('请输入一个四位整数：')
num=int(num)#将num转换为整数类型
print('个位上的数字为：',num%10)
print('十位上的数字为：',num//10%10)
print('百位上的数字为：',num//100%10)
print('千位上的数字为：',num//1000)

#方法二
print('-'*40)
num=input('请输入一个四位整数：')
print('个位上的数字为：',num[3])
print('十位上的数字为：',num[2])
print('百位上的数字为：',num[1])
print('千位上的数字为：',num[0])