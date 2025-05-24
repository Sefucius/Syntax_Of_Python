from queue import Queue
from threading import Thread
import time
# 创建一个生产者类
class Producer(Thread):
    def __init__(self,name,queue):
        super().__init__(name=name) # 调用父类的构造函数
        self.queue=queue 
    def run(self): # 重写run方法，run方法是线程的入口函数，线程启动后会自动执行run方法
        for i in range(1,6): # 生产5个产品
            print(f'{self.name}将第{i}个产品放入队列') 
            self.queue.put(i)
            time.sleep(1) 
        print('生产者完成了所有数据的存放')

# 创建一个消费者类
class Consumer(Thread):
    def __init__(self,name,queue):
        super().__init__(name=name) # 调用父类的构造函数
        self.queue=queue
    def run(self): # 重写run方法，run方法是线程的入口函数，线程启动后会自动执行run方法
        for _ in range(5): # 消费5个产品
            value=self.queue.get() # 从队列中取出一个产品
            print(f'消费者线程{self.name}从队列中取出了{value}')
            time.sleep(1)
        print(f'消费者线程完成了所有数据的取出')

if __name__ == '__main__':
    # 创建一个队列，用于存放产品
    queue=Queue() # 队列的大小是无限的，默认是先进先出
    # 创建生产者线程
    producer=Producer('生产者线程',queue)
    # 创建消费者线程
    consumer=Consumer('消费者线程',queue)
    # 启动线程
    producer.start()
    consumer.start()
    # 等待线程执行完成
    producer.join()
    consumer.join()
    print('主线程执行完成')