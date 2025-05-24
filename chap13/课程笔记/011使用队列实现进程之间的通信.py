from multiprocessing import Process,Queue
import time
a=100

def write_msg(q): # q队列
    global a
    if not q.full(): # 判断队列是否已满
        for i in range(6):
            a-=10
            q.put(a) 
            print('a入队时的值是：',a)

#出队
def read_msg(q):
    time.sleep(1) # 让读操作延迟1秒
    while not q.empty(): # 判断队列是否为空
        print('a出队时的值是：',q.get()) # 从队列中读取数据

if __name__ == '__main__':
    print('主进程开始执行')
    q = Queue() # 任务没有上限
    p1 = Process(target=write_msg, args=(q,)) # 创建一个进程，将队列作为参数传递给子进程
    p2 = Process(target=read_msg, args=(q,)) 
    p1.start() # 启动进程
    p2.start() 
    p1.join() # 等待进程执行完成
    p2.join() 
    print('主进程执行结束')