def my_read(filename):
    # 打开文件
    file=open(filename,'w+',encoding='utf-8')
    # 操作
    file.write('你好啊') # 写入完成，文件的指针在最后
    # 修改文件指针的位置
    file.seek(0)
    # 读取
    # content = file.read() # 读取所有内容
    # content = file.read(2) # 读取指定长度的内容
    # content = file.readline() # 读取一行内容
    # content = file.readline(2) # 读取一行中指定长度的内容
    # content = file.readlines() # 读取所有内容，返回的是一个列表
    # 读取“好啊”
    file.seek(3) # utf-8中，一个中文占3个字节，所以指针要往后移动3个字节
    content = file.read() 
    print(type(content),content)
    # 关闭文件
    file.close()

if __name__ == '__main__':
    my_read('d.txt')
