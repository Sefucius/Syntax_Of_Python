import os
print('当前的工作路径是：',os.getcwd())

# 删除文件
# os.remove(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\aa copy.txt')
# 如果文件不存在，则报错

# 重命名
# os.rename(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\aa copy.txt',r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\newaa.txt')

# 转换时间格式
import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
    return s

# 获取文件信息
info = os.stat(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\newaa.txt')
print(type(info))
print(info)
print('最近一次访问时间:',date_format(info.st_atime))
print('最近一次修改时间:',date_format(info.st_mtime))
print('创建时间:',date_format(info.st_ctime))
print('文件大小(Byte):',info.st_size)

# 启动路径下的文件
os.startfile('calc.exe')
# 启动Python解释器
os.startfile(r'E:\python\python.exe')
