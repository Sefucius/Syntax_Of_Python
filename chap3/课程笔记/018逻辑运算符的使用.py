print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

print('-'*50) # 分隔符

print(8>5 and 8<10) # True
print(8>5 and 8>10) # False
print(8<5 and 8<10) # False
print(8<5 and 8>10) # False

print('-'*50) # 分隔符

print(8<7 and 10/0) # False , 10/0不会运算

print('-'*50) # 分隔符

print(True or True) # True
print(True or False) # True
print(False or False) # False
print(False or True) # True

print('-'*50) # 分隔符

print(8>5 or 10/0) # True，10/0不会运算

print('-'*50) # 分隔符

print(not True) # False
print(not False) # True
print(not 8>5) # False
print(not 8<5) # True


