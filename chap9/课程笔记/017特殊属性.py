class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 创建类的对象
a=A()
b=B()
c=C('梁娜',22)

print('对象a的属性字典：',a.__dict__)
print('对象b的属性字典：',b.__dict__)
print('对象c的属性字典：',c.__dict__)

print('对象a所属的类：',a.__class__)
print('对象b所属的类：',b.__class__)
print('对象c所属的类：',c.__class__)

print('对象c的类的父类：',c.__class__.__bases__)
print('对象c的类的父类的父类：',c.__class__.__bases__[0].__bases__)
print('对象c的类的父类的父类：',c.__class__.__bases__[1].__bases__)

print('A类的父类：',A.__base__)
print('B类的父类：',B.__base__)
print('C类的父类：',C.__base__) # 只显示第一个父类


print('A类的父类：',A.__bases__)
print('B类的父类：',B.__bases__)
print('C类的父类：',C.__bases__) # 显示所有父类组成的元组

print('A类的层次结构:',A.__mro__)
print('B类的层次结构:',B.__mro__)
print('C类的层次结构:',C.__mro__) # 显示所有父类组成的元组

# 子类列表
print('A类的子类列表:',A.__subclasses__())
print('B类的子类列表:',B.__subclasses__())
print('C类的子类列表:',C.__subclasses__()) # 显示所有子类组成的列表