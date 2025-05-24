from multiprocessing import Queue

if __name__ == '__main__':
    # 创建一个队列，最多可以接受3个元素
    q = Queue(3)
    # 向队列中添加元素
    q.put(1)
    q.put(2)
    q.put(3)
    # 向已满的队列中添加元素，会阻塞
    q.put(4,block=True,timeout=2) # 阻塞2秒,2秒后抛出异常
    

