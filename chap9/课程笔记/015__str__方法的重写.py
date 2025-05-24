class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'大家好，我是{self.name}, 今年{self.age}岁。')

    def __str__(self):
        return f'这是一个人类，具有name和age属性。'

p = Person('张三', 18)
print(p)