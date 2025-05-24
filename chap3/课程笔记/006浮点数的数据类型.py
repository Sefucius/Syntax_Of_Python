height=178.8 #身高
print(height)
print(type(height)) #<class 'float'>

x=10
y=10.0
print('x的数据类型是:',type(x)) #<class 'int'>
print('y的数据类型是:',type(y)) #<class 'float'>

x=1.99E1413
print('科学计数法',x,'x的数据类型是:',type(x)) #<class 'float'>
#inf表示正无穷大，-inf表示负无穷大,超出浮点数范围了
print(0.1+0.2) # 不确定的尾数问题 0.30000000000000004

print(round(0.1+0.2,1)) # 0.3

