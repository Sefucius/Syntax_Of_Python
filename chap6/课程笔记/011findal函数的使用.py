import re # 导入
patterm='\d\.\d+'
pattern='\d\.\d+'
s='I study Python 3.11 every day Python 2.7 every day'
s2='4.10 Python I study every day'
s3='Python I study every day'
# 查找所有满足条件的内容，返回一个列表，列表中每个元素都是满足条件的内容
lst=re.findall(pattern,s,re.I) 
lst2=re.findall(pattern,s2,re.I) 
lst3=re.findall(pattern,s3,re.I) 
print(lst)
print(lst2)
print(lst3)