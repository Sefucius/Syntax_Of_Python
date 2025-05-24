# isdigit() 方法检测字符串是否只由数字组成。
print('123'.isdigit())  # True
print('一二三'.isdigit())  # False
print('0b1010'.isdigit())  # False
print('ⅢⅢⅢ'.isdigit())  # False
print('-'*40)
# isnumeric() 方法检测字符串是否只由数字组成。
print('123'.isnumeric())  # True
print('一二三'.isnumeric())  # True
print('0b1010'.isnumeric())  # False
print('ⅢⅢⅢ'.isnumeric())  # True
print('壹贰叁'.isnumeric())  # True
print('-'*40)
# isalpha() 方法检测字符串是否只由字母(包含中文字符)组成。
print('abc'.isalpha())  # True
print('abc123'.isalpha())  # False
print('abc一二三'.isalpha())  # True
print('abc壹贰叁'.isalpha())  # True
print('abcⅢⅢⅢ'.isalpha()) # False
print('-'*40)
# isalnum() 方法检测字符串是否由字母（包含中文）和数字组成。
print('abc'.isalnum())  # True
print('abc123'.isalnum())  # True
print('abc一二三'.isalnum())  # True
print('abc壹贰叁'.isalnum())  # True
print('abcⅢⅢⅢ'.isalnum()) # True
print('-'*40)
# 判断字符的大小写
# 判断字符串是否全是大写
print('HelloWorld'.isupper())  # False
print('HELLOWORLD'.isupper())  # True
print('HELLOWORLD你好'.isupper())  # True
print('-'*40)
# 判断字符串是否全是小写
print('HelloWorld'.islower())  # False
print('helloworld'.islower())  # True
print('helloworld你好'.islower())  # True
print('-'*40)

# 所有字符都是首字母大写，其余小写的情况
print('HelloWorld'.istitle())  # False
print('HelloWorld你好'.istitle())  # False
print('HelloWorld你好'.istitle())  # False
print('Helloworld'.istitle())  # True
print('Hello world'.istitle())  # False

print('-'*40)
# 判断是否空白字符
print(' '.isspace())  # True
print(''.isspace())  # False
print(' \t\n\r'.isspace())  # True
