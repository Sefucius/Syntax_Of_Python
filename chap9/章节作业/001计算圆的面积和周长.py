import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):  # 计算面积
        return math.pi * self.radius * self.radius
    def get_perimeter(self):  # 计算周长
        return 2 * math.pi * self.radius

# 测试
circle = Circle(eval(input("请输入圆的半径：")))
print("圆的面积为：%.2f" % circle.get_area())
print("圆的周长为：%.2f" % circle.get_perimeter ())