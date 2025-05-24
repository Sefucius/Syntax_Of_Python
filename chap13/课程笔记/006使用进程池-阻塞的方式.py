from multiprocessing import Pool
import os, time

# 编写任务
def task(task_name):
    print(f'子进程的PID：{os.getpid()}，执行的任务：{task_name}')
    time.sleep(1)

if __name__ == '__main__':
    # 主进程
    start = time.time()
    print('父进程开始执行')
    # 创建进程池
    pool = Pool(3)
    # 创建任务
    for i in range(10):
        # 以非阻塞的方式
        pool.apply(func=task, args=(f'任务{i}',))

    # 关闭进程池
    pool.close()
    # 阻塞父进程
    pool.join()
    print('所有的子进程执行完毕，父进程执行结束')
    print(time.time()-start)