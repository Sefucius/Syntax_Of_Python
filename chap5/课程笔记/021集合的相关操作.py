s={10,20,30}
# 向集合中添加元素
s.add(100)
print(s)
# 集合元素的删除
s.remove(10)
print(s)
# 集合的清空
s.clear()
print(s)

for i in range(1,11):
    s.add(i)

# 集合的遍历操作
for item in s:
    print(item)

# 使用enumerate()函数进行遍历操作
for index,item in enumerate(s):
    print(index,'----->',item)

# 集合的生成式
s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==1}
print(s)

