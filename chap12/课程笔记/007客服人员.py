from socket import socket, AF_INET, SOCK_DGRAM

# 创建UDP套接字
recv_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定IP地址和端口号
recv_socket.bind(('172.27.96.42', 8888))

while True:
    # 接收数据
    recv_data, recv_addr = recv_socket.recvfrom(1024)
    print(f'客户说：{recv_data.decode("utf-8")}')
    if recv_data.decode('utf-8') == 'bye':
        break
    # 准备回复对方数据
    send_data = input('客服回复：')
    # 发送数据
    recv_socket.sendto(send_data.encode('utf-8'),recv_addr)

# 关闭套接字
recv_socket.close()