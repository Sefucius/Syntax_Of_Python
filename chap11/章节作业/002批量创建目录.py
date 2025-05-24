import random
import os
import os.path as op
def createFolder():
    num = int(input('请输入要创建的目录个数：'))
    # 获取当前的工作路径
    path = op.abspath('.')
    # 判断一个路径是否是有效目录
    if not os.path.exists(fr'{path}\chap11\章节作业\newdir'):
        os.mkdir(fr'{path}\chap11\章节作业\newdir')
    for i in range(num):
        # 创建目录
        os.mkdir(fr'{path}\chap11\章节作业\newdir\{i+1}')

if __name__ == '__main__':
    createFolder()