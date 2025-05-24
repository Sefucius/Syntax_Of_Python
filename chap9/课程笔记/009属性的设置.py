class Student:
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender  # 私有的实例属性

    # @property装饰器把一个方法变成属性调用
    @property
    def gender(self):
        return self.__gender
    # 将gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value!='男' and value!='女':
            print('性别有误，已将性别默认设置为男')
            self.__gender='男'
        else:
            self.__gender=value

stu=Student('梁娜','女')
print(stu.name,'的性别是',stu.gender) # stu.gender执行stu.gender()
# 尝试修改属性值
# stu.gender='男' # 报错，因为gender是只读属性，不能修改

stu.gender='仙女'
print(stu.name,'的性别是',stu.gender)