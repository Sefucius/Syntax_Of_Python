from multiprocessing import Process
import time,os

# 函数中的代码就是子进程要执行的代码
def test():
    print(f'我是子进程，我的PID是{os.getpid()}，我的父进程PID是{os.getppid()}')
    time.sleep(1)
    print(f'我的PID是{os.getpid()},子进程结束')

if __name__ == '__main__':
    print(f'主进程开始执行')
    lst = []
    # 创建5个子进程
    for i in range(5):
        # 创建子进程对象
        p = Process(target=test)
        # 启动子进程
        p.start()
        # 将启动的子进程加入到列表中
        lst.append(p)

    # 遍历lst，让主进程等待子进程执行结束
    for p in lst:
        p.join() # 阻塞主进程

    print(f'主进程执行结束')