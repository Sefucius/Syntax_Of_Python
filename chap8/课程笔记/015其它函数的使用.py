# format
print(format(3.14,'20')) # 数值型默认右对齐
print(format('hello','20'))# 字符串型默认左对齐
print(format('hello','*<20')) # 字符串型左对齐,用*填充,总长度20
print(format('hello','*>20')) # 字符串型右对齐,用*填充,总长度20
print(format('hello','*^20')) # 字符串型居中对齐,用*填充,总长度20


print(format(3.1415926,'.2f')) # 保留小数点后两位,四舍五入
print(format(3.1415926,'.3e')) # 保留小数点后三位,科学计数法
print(format(3.1415926,'.3E')) # 保留小数点后三位,科学计数法,大写E

print(format(20,'b')) # 二进制
print(format(20,'o')) # 八进制
print(format(20,'x')) # 十六进制
print(format(20,'X')) # 十六进制,大写X

print('-' * 30)
print(len('helloworld'))
print(len([10,20,30,40,50]))

print('-' * 30)
print(id(10))
print(id('helloworld'))
print(type('hello'),type(10))

print(eval('10+30'))
print(eval('10>30'))