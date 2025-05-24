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

# 创建实例对象
s1=Student('黄文浩',22)
s2=Student('梁娜',22)
print(s1.name,s1.age) # 输出：黄文浩 22
print(s2.name,s2.age) # 输出：梁娜 22

# 动态绑定属性
s2.gender='男'
print(s2.name,s2.age,s2.gender)

# print(s1.gender) # 报错，stu对象没有gender属性

# 动态绑定方法
def introduce():
    print(f'我是一个普通的函数，我被动态绑定成了stu2的方法')
s2.fun=introduce # 动态绑定方法，将函数作为属性赋值给实例对象
s2.fun() 
