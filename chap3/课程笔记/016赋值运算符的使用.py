x=20 # 直接赋值，将20赋值给x
y=10 # 直接赋值，将10赋值给y
x=x+y # 将x+y的结果赋值给x
print(x) 
x+=y # 将x+y的结果赋值给x
print(x) #40
x-=y # 将x-y的结果赋值给x
print(x) #30
x*=y # 将x*y的结果赋值给x
print(x) #300
x/=y # 将x/y的结果赋值给x
print(x)        #发生了类型转换，x=30.0
print(type(x)) 
x%=y # 将x%y的结果赋值给x
print(x) #0.0
z=3
y//=z # 将y//z的结果赋值给y,整除,结果为3
print(y) #3
y**=z # 将y**z的结果赋值给y,幂运算,结果为27
print(y) #27

# Python支持链式赋值
a=b=c=100 # 将100赋值给a,b,c
print(a,b,c) #100 100 100

# Python支持系列解包赋值
a,b,c=1,2,3 # 将1赋值给a,2赋值给b,3赋值给c
print(a,b,c) #1 2 3

print('--------如何交换两个变量的值呢？---------')
# Python支持交换变量值
a,b=1,2
a,b=b,a # 将b的值赋值给a,将a的值赋值给b
print(a,b) #2 1

