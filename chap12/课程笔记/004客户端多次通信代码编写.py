import socket

# 创建socket对象
client_socket = socket.socket()
# 主机的IP地址和端口号
client_socket.connect(('172.27.96.42', 8888))
print('--------已建立服务器连接--------')
# 客户端发送数据
info=''
while info!='bye':
    # 准备发送数据
    send_data = input('请客户端输入要发送的数据:')
    client_socket.send(send_data.encode('utf-8')) # 发送数据
    if send_data == 'bye':
        break
    # 接收服务器端发送的数据
    info = client_socket.recv(1024).decode('utf-8') # 接收数据
    print(f'服务器端发送过来的数据为:{info}')
# 关闭连接
client_socket.close()