import json
# 准备高维数据
lst=[
    {'name':'zs','age':18,'score':'90'},
    {'name':'ls','age':19,'score':'91'},
    {'name':'ww','age':20,'score':'92'}
]
# 编码
s=json.dumps(lst,ensure_ascii=False,indent=4) # ensure_ascii正常显示中文 indent=4 缩进4个空格 美观
print(type(s)) # list转str
print(s)

# 解码
lst2=json.loads(s)
print(type(lst2)) # str转list
print(lst2)

# 编码到文件中
with open('student.txt','w',encoding='utf-8') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4) # 编码到文件中

# 解码到程序中
with open('student.txt','r',encoding='utf-8') as file:
    lst3=json.load(file) # 从文件中解码
    print(type(lst3)) # str转list
    print(lst3)