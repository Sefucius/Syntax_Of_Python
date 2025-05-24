from multiprocessing import Queue

if __name__ == "__main__":
    # 创建一个队列，最多可接受3个任务
    q = Queue(3)
    print('队列是否为空:', q.empty())
    print('队列是否已满:', q.full())
    # 向队列中添加任务
    q.put('任务1')
    q.put('任务2')
    print('队列是否为空:', q.empty())
    print('队列是否已满:', q.full())
    q.put('任务3')
    print('队列是否为空:', q.empty())
    print('队列是否已满:', q.full())
    print('队列当中任务的个数:', q.qsize())
    # 出队
    print(q.get())
    print('队列当中任务的个数:', q.qsize())
    # 入队
    q.put_nowait('任务4')
    # q.put_nowait('任务5')  # 队列已满，无法添加任务，会报错
    # q.put('任务5')  # 队列已满，无法添加任务，会阻塞
    # 遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())  # 出队，不阻塞

    print('队列是否为空:', q.empty())
    print('队列是否已满:', q.full())
    print('队列当中任务的个数:', q.qsize())