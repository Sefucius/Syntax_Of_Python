from socket import socket, AF_INET, SOCK_DGRAM

# 创建UDP套接字
send_socket = socket(AF_INET, SOCK_DGRAM)

#
while True:
    # 准备发送的数据
    send_data = input('客户说：')
    # 发送数据
    send_socket.sendto(send_data.encode('utf-8'), ('172.27.96.42', 8888))
    if send_data == 'bye':
        break
    # 接收客服回复的数据
    recv_data, recv_addr = send_socket.recvfrom(1024)
    print(f'客服回复：{recv_data.decode("utf-8")}')

# 关闭套接字
send_socket.close()