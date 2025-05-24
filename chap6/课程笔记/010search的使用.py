import re
pattern='\d\.\d+'
s='I study Python 3.11 every day Python 2.7 every day'
match=re.search(pattern,s,re.I) 

s2='4.10 Python I study every day'
s3='Python I study every day'
match2=re.search(pattern,s2,re.I)
match3=re.search(pattern,s3,re.I)
print(match) 
print(match2)
print(match3)

print(match.group())
print(match2.group())
