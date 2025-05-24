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


# 创建对象
s1=Student('hwh',22)
s2=Student('ln',22)
s3=Student('love',21)
s4=Student('happy',99)

print(type(s1)) # <class '__main__.Student'>
print(type(s2)) 
print(type(s3)) 
print(type(s4)) 

Student.school='北京大学' # 给类属性赋值

# 将学生对象存储到列表中
lst=[s1,s2,s3,s4]
for item in lst:
    item.show()