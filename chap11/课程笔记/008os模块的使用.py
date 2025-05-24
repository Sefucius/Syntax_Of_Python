import os
print('当前的工作路径是：',os.getcwd())
lst=os.listdir()
print('当前路径下的所有目录及文件:',lst)
print('指定路径下的所有目录及文件:',os.listdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记'))
# 创建目录
# os.mkdir('我爱娜娜') # 如果目录存在，则报错
# os.makedirs('.aa/bb/cc') # ./表示当前目录，../表示上级目录
# 删除目录
# os.rmdir('我爱娜娜') # 如果目录不存在，则报错
# os.removedirs('.aa/bb/cc') 

# 改变当前的工作路径
os.chdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记')
print('当前的工作路径是：',os.getcwd())
# 遍历目录树
for dirs,dirlst,filelst in os.walk('E:\Microsoft Visual Studio\Project\Python_learning'):
    print('当前目录是：',dirs)
    print('当前目录下的所有子目录是：',dirlst)
    print('当前目录下的所有文件是：',filelst)
    print('-'*20)