from socket import socket, AF_INET, SOCK_DGRAM

# 创建UDP套接字
recv_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定IP地址和端口号
recv_socket.bind(('172.27.96.42', 8888))

# 接收来自发送方的数据
recv_data, recv_addr = recv_socket.recvfrom(1024)
print(f'接收的数据为：{recv_data.decode("utf-8")}')

# 准备回复对方的数据
reply_data =input("请输入要回复的数据：")

# 发送回复数据给发送方
recv_socket.sendto(reply_data.encode('utf-8'), recv_addr)

# 关闭UDP套接字
recv_socket.close()