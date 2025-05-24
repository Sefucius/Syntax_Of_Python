s='HelloWorld'
# 字符串的替换
new_s=s.replace('o','你好',1) 
# 最后一个参数表示替换的次数，默认是全部替换
print(new_s)

# 字符串在指定范围内居中
print(s.center(20))
print(s.center(20,'*'))

# 去掉字符串左右两边的空格
s='   Hello   World   '
print(s.strip())
# 去掉字符串左边的空格
print(s.lstrip())
# 去掉字符串右边的空格
print(s.rstrip())

# 去掉指定的字符
s3='dl-HelloWorld'
print(s3.strip('ld')) # 与顺序无关
print(s3.lstrip('dl'))
print(s3.rstrip('dl'))