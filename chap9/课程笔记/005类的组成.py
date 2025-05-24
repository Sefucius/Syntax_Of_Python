class Student:
    # 类属性,定义在类里面,方法外面的变量
    school='中山大学'

    # 初始方法方法
    def __init__(self,name,age):
        # name,age是局部变量,只能在init方法里面使用
        self.name=name # =左侧是实例属性
        self.age=age # 实例的名称和局部变量的名称可以相同
        
    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫{self.name},今年{self.age}岁了')

    # 静态方法,不需要self参数
    @staticmethod
    def sm():
        # print(self.name) 报错
        # self.show() 报错
        print('这是一个是静态方法，不能调用实例属性，也不能调用实例方法。')

    @classmethod
    def cm(cls): # cls-->class的缩写
        # print(self.name) 报错
        # self.show() 报错
        print('这是一个是类方法，不能调用实例属性，也不能调用实例方法。')

# 创建类的对象
s1=Student('张三',20) # s1是实例对象，自动调用__init__()方法
# 实例属性，使用对象名称进行打点调用
print(s1.name,s1.age) # 张三 20
# 类属性，使用类名称进行打点调用
print(Student.school) # 中山大学
# 实例方法，使用对象名称进行打点调用
s1.show() # 我叫张三,今年20岁了
# 类方法，使用类名称进行打点调用
Student.cm()
# 静态方法，使用类名称进行打点调用
Student.sm() 