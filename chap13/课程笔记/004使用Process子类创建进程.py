from multiprocessing import Process
import time,os

# 自定义一个类
class SubProcess(Process):
    # 编写一个初始化方法
    def __init__(self,name):
        # 调用父类的初始化方法
        super().__init__()
        self.name = name
    # 重写父类的run方法
    def run(self):
        print("子进程的名字是：",self.name,"\n子进程的PID是：",os.getpid(),"\n父进程的PID是：",os.getppid())

if __name__ == '__main__':
    print('父进程开始运行')
    lst=[]
    for i in range(5):
        p1 = SubProcess("子进程"+str(i+1))
        p1.start()
        lst.append(p1)

    # 阻塞一下主进程
    for p in lst:
        p.join()
    print("父进程结束运行")
    