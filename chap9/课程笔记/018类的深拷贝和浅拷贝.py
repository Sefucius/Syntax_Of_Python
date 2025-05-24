class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk


cpu=CPU()
disk=Disk()

c1=Computer(cpu,disk)

c2=c1 # 变量的赋值操作，是将变量的内存地址赋值给新的变量，而不是拷贝对象。
print(c1,'子对象的内存地址：',c1.cpu,c1.disk)
print(c2,'子对象的内存地址：',c2.cpu,c2.disk)

print('-'*50)
import copy
c3=copy.copy(c1)  # 浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象。
print(c1,'子对象的内存地址：',c1.cpu,c1.disk)
print(c3,'子对象的内存地址：',c3.cpu,c3.disk)

print('-'*50)
c4=copy.deepcopy(c1)  # 深拷贝，拷贝对象及其子对象
print(c1,'子对象的内存地址：',c1.cpu,c1.disk)
print(c4,'子对象的内存地址：',c4.cpu,c4.disk)