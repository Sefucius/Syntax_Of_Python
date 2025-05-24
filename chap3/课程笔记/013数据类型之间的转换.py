
x=10
y=3
z=x/y # 在执行除法运算的时候，将运算的结果赋值给z
print(z,type(z)) # 隐式转换，通过运算隐式地转换了结果的类型

# float类型转成int类型，只保留整数部分
print('float类型转成int类型：',int(3.14))
print('float类型转成int类型：',int(3.9))
print('float类型转成int类型：',int(-3.14))
print('float类型转成int类型：',int(-3.9))

# 将int转成float类型
print('将int转成float类型',float(10))
# 将str转成int类型
print(int('100')+int('200'))

''' 
    将字符串转成int或float时报错的情况
    print(int('18a')) 
    print(int('3.14'))
    print(float('45a.987'))
'''

# chr()和ord()查询unicode表
print(ord('黄')) #黄在unicode表中对应的整数值
print((chr(40644))) # 40644整数在unicode表中对应的字符是什么

# 进制之间的转换操作，十进制与其它进制之间的转换
print('十进制转成十六进制：',hex(26472))
print('十进制转成八进制：',oct(26472))
print('十进制转成二进制：',bin(26472))
print(type(hex(26472)))
print(type(oct(26472)))
print(type(bin(26472))) #转换后是字符串类型

print('----------------------')
print('十六进制转成十进制：',int('0x6768',16))
print('八进制转成十进制：',int('0o63650',8))
print('二进制转成十进制：',int('0b110011101100100',2))
print('----------------------')
