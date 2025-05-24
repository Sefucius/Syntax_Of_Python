s1='hello'
s2='world'
# + 拼接字符串
s3=s1+s2
print(s3)
# join 拼接字符串
s3=''.join([s1,s2])
print(s3)
print('*'.join(['hello','world','python','java','php']))
print('你好'.join(['hello','world','python','java','php']))
# 直接拼接字符串
s3='hello''world'
print(s3)
# 格式化字符串
s3=f'{s1}{s2}'
print(s3)
# % 拼接字符串
s3='%s%s'%(s1,s2)
print(s3)
# format 拼接字符串
s3='{0}{1}'.format(s1,s2)
print(s3)