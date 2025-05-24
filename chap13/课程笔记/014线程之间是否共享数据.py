from threading import Thread
a=100
def add():
    print(f'加线程开始执行')
    global a
    a+=30
    print(f'a的值为{a}')
    print(f'加线程执行完成')

def sub():
    print(f'减线程开始执行')
    global a
    a-=50
    print(f'a的值为{a}')
    print(f'减线程执行结束')

if __name__ == '__main__':
    print('主线程开始执行')
    print(f'全局变量a的值为{a}')
    t1=Thread(target=add)
    t2=Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程执行结束')

    # 线程之间的数据是共享的
    