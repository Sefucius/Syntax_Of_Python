t=('python','hello','world')
# 根据索引访问元组
print(t[0]) 
t2=t[0:3:2] # 元组支持切片操作
print(t2)

# 元组的遍历
for item in t:
    print(item)

# for+range()+len()
for i in range(len(t)):
    print(i,t[i])

# 使用enumerate()函数进行遍历
for index,item in enumerate(t):
    print(index,'----->',item)

# 序号从11开始
for index,item in enumerate(t,start=11):
    print(index,'----->',item)