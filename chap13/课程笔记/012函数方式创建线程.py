import threading
from threading import Thread
import time
# 编写函数
def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程:{threading.current_thread().name}正在执行{i}')

if __name__ == '__main__':
    start=time.time()
    print('主线程开始执行')

    # 创建线程
    lst =[Thread(target=test) for i in range(2)]
    # 启动线程
    for t in lst: # t的数据类型是Thread
        # 启动线程
        t.start()

    for t in lst: # t的数据类型是Thread
        # 等待线程执行完成
        t.join()

    end=time.time()
    print(f'主线程执行完成,耗时:{end-start}')

    # 三个线程并行执行的任务是什么？
    # 主线程负责执行main函数中的代码，
    # Thread-1线程执行三次循环
    # Thread-2线程执行三次循环
    # 三个线程又是并发执行，谁先执行不一定