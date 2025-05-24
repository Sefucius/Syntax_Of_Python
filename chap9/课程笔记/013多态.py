class Person():
    def eat(self):
        print("人吃五谷杂粮")

class Cat():
    def eat(self):
        print("猫吃鱼")

class Dog():
    def eat(self):
        print("狗吃肉")

# 这三个类中都有一个同名的方法eat()
# 编写函数
def fun(obj):
    obj.eat() # 通过obj(对象),调用eat()方法

per=Person()
cat=Cat()
dog=Dog()

fun(per) # 人吃五谷杂粮
fun(cat) # 猫吃鱼
fun(dog) # 狗吃肉