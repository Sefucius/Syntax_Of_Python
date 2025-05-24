import random
import os

# 修改当前的工作路径
os.chdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\章节作业\data')
# print('当前的工作路径是：',os.getcwd())

def createfile(i):
    for j in range(i):
        # 随机生成8位十六进制数
        random_str = ''.join([random.choice('0123456789ABCDEF') for j in range(8)])
        # print('{0:0>4}'.format(i)) # 右对齐，总宽度4，空白用0填充
        s='{0:0>4}'.format(str(j+1))
        lst=['肉蛋','水果','蔬菜','粮油','烟酒']
        # 创建文件
        file=open(f'{s}_{lst[random.randint(0,4)]}_{random_str}.txt','w',encoding='utf-8')
        # 关闭文件
        file.close()

if __name__ == '__main__':
    createfile(3000)
    # # 删除指定目录下的所有文件
    # for i in os.listdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\章节作业\data'):
    #     os.remove(i)