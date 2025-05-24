class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'大家好，我是{self.name}, 今年{self.age}岁。')

# 创建对象
p1 = Person('张三', 18)
print(dir(p1)) # 查看对象的属性和方法

print(p1) # 自动调用__str__方法，打印对象的内存地址
print(p1.__str__()) # 手动调用__str__方法，打印对象的内存地址