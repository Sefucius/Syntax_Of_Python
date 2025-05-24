a=10
b=20
print(dir(a)) # Python中一切皆对象
print(a+b)
print(a.__add__(b))
print(a.__sub__(b)) # 减法

print(a.__mul__(b)) # 乘法
print(a.__truediv__(b)) # 除法

print(a.__floordiv__(b)) # 整除
print(a.__mod__(b)) # 取余

print(a.__pow__(b)) # 幂运算

print(f'{a}<{b}吗？',a.__lt__(b))
print(f'{a}<={b}吗？',a.__le__(b))

print(f'{a}>{b}吗？',a.__gt__(b))
print(f'{a}>={b}吗？',a.__ge__(b))

print(f'{a}=={b}吗？',a.__eq__(b)) 
print(f'{a}!={b}吗？',a.__ne__(b))