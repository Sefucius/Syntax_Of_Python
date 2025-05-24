import socket

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机和IP端口
server_socket.bind(('172.27.96.42', 8888)) 

# 设置最大连接数量
server_socket.listen(5)

# 等待客户端TCP连接
client_socket, client_address = server_socket.accept()
print(f'客户端{client_address}已连接')

# 接收数据
data = client_socket.recv(1024).decode('utf-8') # while循环的四个步骤，data是初始化变量

while data != 'bye':  # 条件判断
    if data != '':
        print(f'客户端{client_address}发送过来的数据为:{data}')
    # 准备待发送的数据
    data = input('请输入要发送给客户端的数据:')
    # 发送数据
    client_socket.send(data.encode('utf-8'))
    if data == 'bye':
        break                           # 20-27行 循环体
    data = client_socket.recv(1024).decode('utf-8') # 接收客户端发送的data数据 # 改变变量

# 关闭连接
client_socket.close()
server_socket.close()