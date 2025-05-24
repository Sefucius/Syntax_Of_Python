# 存储和读取一维数据
def my_write():
    # 一维数据可以使用列表、元组、集合
    lst=['张三','李四','王五','赵六','田七']
    with open('student.csv','w',encoding='GBK') as file:
        file.write(','.join(lst)) # 将列表转换为字符串，用逗号分隔

def my_read():
    with open('student.csv','r',encoding='GBK') as file:
        lst=file.read().split(',') # 读取文件内容，用逗号分隔，转换为列表
        print(lst) # 打印列表

# 存储和读取二维数据
def my_write_table():
    lst=[
        ['商品名称','单价','数量'],
        ['苹果','5','10'],
        ['香蕉','3','20'],
        ['橙子','4','15'],
    ]
    with open('goods.csv','w',encoding='GBK') as file:
        for i in lst: # 遍历列表
            file.write(','.join(i)+'\n') # 将列表转换为字符串，用逗号分隔，写入文件
        
def my_read_table():
    data=[] # 定义一个空列表，用于存储二维数据
    with open('goods.csv','r',encoding='GBK') as file:
       lst=file.readlines() # 读取文件内容，按行读取，转换为列表
       for i in lst: # 遍历列表
           data.append(i.strip().split(',')) # 去除字符串两端的空格和换行符，用逗号分隔，转换为列表，添加到data列表中
    print(data) # 打印二维数据


if __name__ == '__main__':
    my_write() # 调用函数，写入文件
    my_read() # 调用函数，读取文件
    my_write_table() # 调用函数，写入文件
    my_read_table() # 调用函数，读取文件