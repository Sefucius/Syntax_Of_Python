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
    print('父进程开始运行')
    print(f'主进程PID:{os.getpid()}')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process, args=('one',))
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=('two',))
        # 启动进程
        p1.start()
        p2.start()
        print(p1.name,'是否处于活跃状态:',p1.is_alive())
        print(p2.name,'是否处于活跃状态:',p2.is_alive())

        print(p1.name,'pid是:',p1.pid)
        print(p2.name,'pid是:',p2.pid)

        # 主进程等待子进程执行完毕后再执行
        p1.join()
        p2.join()
        print(p1.name,'是否处于活跃状态:',p1.is_alive())
        print(p2.name,'是否处于活跃状态:',p2.is_alive())
    print('父进程执行完毕')
