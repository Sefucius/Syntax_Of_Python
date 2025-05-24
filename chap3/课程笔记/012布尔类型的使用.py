x=True
print(x)
print(type(x))
print(x+10) # True+10=11
print(x+False) # True+False=1
print(False+10) # False+10=10

#False=0 True=1

print('------------------')
print(bool(0),bool(0.0)) # False
print(bool(1)) # True
print(bool(18)) # True

# 非0的数的布尔值都是True，0是False

print('------------------')
print(bool('北京欢迎你')) # True
print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool(set())) # False
print(bool(tuple())) # False
print(bool(None)) # False

# 非空字符串的布尔值都是True，空字符串是False

print('------------------')
print(bool(False)) # False
print(bool(True)) # True
print(bool(None)) # False

# False、None的布尔值都是False