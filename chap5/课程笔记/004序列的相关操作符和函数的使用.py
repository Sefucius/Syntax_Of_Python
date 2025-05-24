s='helloworld'

# in的使用
print('e在helloworld中存在吗？',('e' in s)) 
print('v在helloworld中存在吗？',('v' in s)) 

# not in的使用
print('e在helloworld中不存在吗？',('e' not in s))
print('v在helloworld中不存在吗？',('v' not in s))

# 内置函数的使用
print('len()',len(s)) # 序列的长度
print('max()',max(s)) # 序列的最大值
print('min()',min(s)) # 序列的最小值

# 序列对象的方法，使用序列的名称，打点调用
print('s.index()',s.index('o')) # o在s中第一次出现的索引位置
# print('s.index()',s.index('v')) # 不存在，ERROR

print('s.count()',s.count('o')) # o在s中出现的次数