import os.path
print('当前的工作路径是：',os.getcwd())
print('获取文件或目录的绝对路径：',os.path.abspath('随便填什么，可以不填，只留引号'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists(r'chap11\课程笔记\newaa.txt')) # 填相对路径
print('拼接路径:',os.path.join(r'chap11\课程笔记','aa.txt'))
print('分割文件名和文件后缀名:',os.path.splitext('aa.txt')) # 元组形式返回
print('获取文件名:',os.path.basename(r'chap11\课程笔记\newaa.txt')) 
print('获取目录名:',os.path.dirname(r'chap11\课程笔记\newaa.txt')) 
print('判断是否是绝对路径:',os.path.isabs(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\newaa.txt')) 
print('判断一个路径是否是文件:',os.path.isfile(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\aa.txt'))
print('判断一个路径是否是有效目录:',os.path.isdir(r'chap11\课程笔记'))