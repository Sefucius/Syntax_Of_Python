s='helloworldhelloworldasdsijjhdaisdsaidj'
# 字符串拼接及not in的方式
new_s=''
for i in s:
    if i not in new_s:
        new_s+=i
print(new_s)

# 索引+not in的方式
new_s=''
for i in range(len(s)):
    if s[i] not in new_s:
        new_s+=s[i]
print(new_s)

# 集合的方式+列表排序
new_s=set(s)
print(new_s)
lst=list(new_s) # 集合不能排序，所以需要转换为列表
lst.sort(key=s.index) # 列表排序，key=s.index表示按照字符串的索引排序
print(''.join(lst))
