class Student:
    # 类属性,定义在类里面,方法外面的变量
    school='中山大学'

    # 初始方法方法
    def __init__(self,name,age):
        # name,age是局部变量,只能在init方法里面使用
        self.name=name # =左侧是实例属性
        self.age=age # 实例的名称和局部变量的名称可以相同
        