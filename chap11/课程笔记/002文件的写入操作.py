def my_write(s):
    # 打开文件
    file=open('b.txt','a',encoding='utf-8')
    # 写入内容
    file.write(s)
    file.write('\n')
    # 关闭文件
    file.close()

def my_write_list(file,lst):
    # 打开文件
    file=open(file,'a',encoding='utf-8')
    # 操作文件
    file.writelines(lst)
    # 关闭文件
    file.close()

if __name__ == '__main__':
    # my_write('我爱娜娜')
    # my_write('娜娜小宝贝')
    lst=['姓名\t','年龄\t','成绩\t','张三\t','30\t','100\n']
    my_write_list('c.txt',lst)
