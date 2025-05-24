def copy(src,new_path):
    # 文件的复制就是边读边写操作
    # 打开源文件
    file1 = open(src,'rb')
    # 打开目标文件
    file2 = open(new_path,'wb') 
    # 开始复制，边读边写
    s=file1.read()
    file2.write(s)
    # 关闭文件
    file1.close()
    file2.close() # 先打开的后关闭，后打开的先关闭

if __name__ == "__main__":
    src = r'E:\Microsoft Visual Studio\Project\Python_learning\baidu.jpg'
    new_path = r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\baidu_copy.jpg'
    copy(src,new_path)
    print('复制完成')