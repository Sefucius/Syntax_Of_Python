import threading
from threading import Thread
import time
ticket=50

def sale_ticket():
    global ticket
    # 每个排队窗口假设有100人
    for i in range(100):
        if ticket>0:
            print(f'窗口{threading.current_thread().name}正在出售第{ticket}张票')
            ticket-=1
            time.sleep(1) 

if __name__ == '__main__':
    for i in range(3): # 创建三个线程
        t=Thread(target=sale_ticket) # 创建线程对象
        t.start() # 启动线程