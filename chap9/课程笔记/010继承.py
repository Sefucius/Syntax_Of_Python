class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我是{self.name},今年{self.age}岁了')

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age) #调用父类的__init__方法
        self.score = score
    def show(self):
        print(f'大家好，我是{self.name},今年{self.age}岁了，我的分数是{self.score}分')

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age) #调用父类的__init__方法
        self.department = department
    def show(self):
        print(f'大家好，我是{self.name},今年{self.age}岁了，我的科室是{self.department}')



# 创建第一个子类对象
stu=Student('梁娜',22,100)
stu.show()

doctor=Doctor('黄文浩',22,'新凯来')
doctor.show()