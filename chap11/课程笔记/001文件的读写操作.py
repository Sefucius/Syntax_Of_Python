def my_write():
    # 打开文件
    file=open('a.txt','w',encoding='utf-8')
    # 操作文件
    file.write('我爱娜娜')
    # 关闭文件
    file.close()

# 读取文件
def my_read():
    # 打开文件
    file=open('a.txt','r',encoding='utf-8')
    # 操作文件
    content=file.read()
    print(type(content),content)
    # 关闭文件
    file.close()

if __name__ == '__main__':
    my_write()
    my_read()