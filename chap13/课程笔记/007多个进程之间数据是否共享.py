from multiprocessing import Process

a=100

def add():
    print('子进程1开始执行')
    global a
    a+=30
    print('a=',a)
    print('子进程1执行结束')

def sub():
    print('子进程2开始执行')
    global a
    a-=50
    print('a=',a)
    print('子进程2执行结束')

if __name__ == '__main__':
    print('主进程开始执行')
    print('a=',a)
    p1=Process(target=add)
    p2=Process(target=sub)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程执行结束')
    print('a=',a)