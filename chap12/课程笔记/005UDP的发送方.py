from socket import socket, AF_INET, SOCK_DGRAM

# 创建socket对象
send_socket = socket(AF_INET, SOCK_DGRAM)

# 准备发送数据
data=input("请输入要发送的数据：")

# 指定接收方的IP地址和端口号
ip_port=('172.27.96.42', 8888)

# 发送数据
send_socket.sendto(data.encode('utf-8'), ip_port)

# 接收数据
recv_data, recv_addr = send_socket.recvfrom(1024)
print(f'接收的数据为：{recv_data.decode("utf-8")}')

# 关闭socket对象
send_socket.close()