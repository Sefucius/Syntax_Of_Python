import threading
from threading import Thread
import time

class SubThread(Thread):
    def run(self): # 重写run方法，run方法是线程执行的入口
        for i in range(3):
            time.sleep(1)
            print(f'线程:{threading.current_thread().name}正在执行{i}')

if __name__ == '__main__':
    start=time.time()
    print('主线程开始执行')

    # 创建线程
    lst =[SubThread() for i in range(2)]
    # 启动线程
    for t in lst: # t的数据类型是Thread
        # 启动线程
        t.start()

    for t in lst: # t的数据类型是Thread
        # 等待线程执行完成
        t.join()

    end=time.time()
    print(f'主线程执行完成,耗时:{end-start}')