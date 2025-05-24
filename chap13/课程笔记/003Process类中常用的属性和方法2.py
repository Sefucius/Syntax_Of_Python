from multiprocessing import Process
import time
import os

# 函数式方式创建子进程
def sub_process(name):
    print(f'子进程PID:{os.getpid()}, 父进程PID:{os.getppid()},-----------{name}')
    time.sleep(1)

def sub_process2(name):
    print(f'子进程PID:{os.getpid()}, 父进程PID:{os.getppid()},-----------{name}')
    time.sleep(1)

if __name__ == '__main__':
    # 主进程
    print('主进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process() # 没有给定target，不会执行自己编写函数中的代码，会调用Process类中的run方法，run中什么都没有
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=('p2',)) # 给p2进程指定函数，args是一个元组，元组中只有一个元素，需要在元素后面加一个逗号

        # 启动进程
        p1.start() # 没有给定target，会调用Process类中的run方法，run中什么都没有
        p2.start() # 如果指定了target，会执行自己编写的函数中的代码

        # 终止进程
        p1.terminate() # 终止p1进程，不会等待p1进程执行结束，会立即终止p1进程，不会执行p1进程中的代码，会执行主进程中的代码
        p2.terminate() # 终止p2进程，不会等待p2进程执行结束，会立即终止p2进程，不会执行p2进程中的代码，会执行主进程中的代码
    print('主进程执行结束')