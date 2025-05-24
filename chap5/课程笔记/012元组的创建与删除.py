t=('hello',[10,20,30],'python','world')
print(t)

# 使用内置函数tuple()创建元组
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在',(10 in t))
print('10在元组中是否不存在',(10 not in t))
print('最大值',max(t))
print('最小值',min(t))
print('元组的长度',len(t))
print('元组的元素个数t.count:',t.count(10))
print('元组的元素的索引t.index:',t.index(10))

# 如果元组只有一个元素
t=(10)
print(t,type(t)) # <class 'int'>

# 如果元组只有一个元素，需要在元素后面添加逗号
t=(10,)
print(t,type(t)) # <class 'tuple'>

# 元组的删除操作
del t
#print(t) # 报错