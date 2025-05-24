import re # 导入正则表达式模块
pattern='\d\.\d+' 
# +表示匹配前面的字符一次或多次
# \d表示匹配一个数字
# .表示匹配任意字符
# 所以\d\.\d+表示匹配一个数字，后面跟着一个点，再跟着一个数字
string='I study Python 3.11 every day' #待匹配的字符串
match=re.match(pattern,string,re.I)
 #使用re.match()函数进行匹配
 #re.I表示忽略大小写
print(match) #输出匹配结果
s2='3.11 Python I study every day'
match2=re.match(pattern,s2,re.I) #使用re.match()函数进行匹配
print(match2) #输出匹配结果

print('匹配值的起始位置：',match2.start())
print('匹配值的结束位置：',match2.end())
print('匹配区间的位置元素：',match2.span())
print('待匹配的字符串：',match2.string)
print('匹配的数据：',match2.group())
