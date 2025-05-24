# 正向递增
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')

print('\n-----------------')

# 反向递减
for i in range(-len(s),-1):
    print(i,s[i],end='\t\t')

print('\n-----------------')

# 切片
for i in range(len(s)-1,-1,-1):
    print(i,s[i],end='\t\t')