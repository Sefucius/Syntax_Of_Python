class Student():
    # 首尾双下划线
    def __init__(self, name, age, sex):
        self._name = name # self._name 受保护的，只能本类和子类访问
        self.__age = age # self.__age 私有的，只能本类访问
        self.sex = sex # self.sex 普通的实例属性，类的内部外部，子类都可以访问
    def _fun1(self):
        print('类及子类可以访问')
    def __fun2(self):
        print('本类可以访问')
    def show(self): # 普通的实例方法
        self._fun1() # 类本身访问受保护的方法
        self.__fun2() # 类本身访问私有的方法
        print(self._name) # 类本身访问受保护的属性
        print(self.__age) # 类本身访问私有的属性

# 实例化
stu = Student('张三', 18, '男')

print(stu._name) # 类的外部访问受保护的属性
# print(stu.__age) # 类的外部访问私有的属性，报错

stu._fun1() # 类的外部访问受保护的方法
# stu.__fun2() # 类的外部访问私有的方法，报错

stu.show() # 类的外部访问普通的实例方法

# 访问私有属性和方法
print(stu._Student__age) # 类的外部访问私有的属性，不推荐
stu._Student__fun2() # 类的外部访问私有的方法，不推荐

print(dir(stu)) # 查看对象的属性和方法，包含私有属性和方法