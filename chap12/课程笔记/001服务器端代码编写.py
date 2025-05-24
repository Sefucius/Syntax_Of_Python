from socket import socket,AF_INET,SOCK_STREAM
# AF_INET代表IPV4，用于Internet之间的进程通信
# SOCK_STREAM代表TCP协议

# 创建socket对象
server_socket = socket(AF_INET,SOCK_STREAM)
# 绑定IP和端口
ip = '172.27.96.42' # 本机IP
port = 8888 # 端口
server_socket.bind((ip,port))

# 监听
server_socket.listen(5) # 最多允许5个客户端连接
print('服务器已启动，等待客户端连接...')

# 等待客户端连接
client_socket,client_address = server_socket.accept() # 系列解包赋值
print('客户端已连接:',client_address)

# 接收客户端发送的数据
data = client_socket.recv(1024) # 1024代表一次最多接收1024字节的数据
print('客户端发送过来的数据为:',data.decode('utf-8')) # 解码

# 关闭socket
server_socket.close()





# 以太网适配器 以太网:

#    媒体状态  . . . . . . . . . . . . : 媒体已断开连接
#    连接特定的 DNS 后缀 . . . . . . . :

# 无线局域网适配器 本地连接* 1:

#    媒体状态  . . . . . . . . . . . . : 媒体已断开连接
#    连接特定的 DNS 后缀 . . . . . . . :

# 无线局域网适配器 本地连接* 2:

#    媒体状态  . . . . . . . . . . . . : 媒体已断开连接
#    连接特定的 DNS 后缀 . . . . . . . :

# 以太网适配器 VMware Network Adapter VMnet1:

#    连接特定的 DNS 后缀 . . . . . . . :
#    本地链接 IPv6 地址. . . . . . . . : fe80::415:a0e2:f2c2:5dec%10
#    IPv4 地址 . . . . . . . . . . . . : 192.168.23.1
#    子网掩码  . . . . . . . . . . . . : 255.255.255.0
#    默认网关. . . . . . . . . . . . . :

# 以太网适配器 VMware Network Adapter VMnet8:

#    连接特定的 DNS 后缀 . . . . . . . :
#    本地链接 IPv6 地址. . . . . . . . : fe80::3f38:cbfc:6594:741d%15
#    IPv4 地址 . . . . . . . . . . . . : 192.168.106.1
#    子网掩码  . . . . . . . . . . . . : 255.255.255.0
#    默认网关. . . . . . . . . . . . . :

# 无线局域网适配器 WLAN:

#    连接特定的 DNS 后缀 . . . . . . . :
#    IPv6 地址 . . . . . . . . . . . . : 2001:250:3002:3250::1317
#    本地链接 IPv6 地址. . . . . . . . : fe80::8928:de33:35ba:c02%5
#    IPv4 地址 . . . . . . . . . . . . : 172.27.96.42
#    子网掩码  . . . . . . . . . . . . : 255.255.128.0
#    默认网关. . . . . . . . . . . . . : fe80::5a69:6cff:fed1:c1f3%5
#                                        172.27.0.1

# 以太网适配器 蓝牙网络连接:

#    媒体状态  . . . . . . . . . . . . : 媒体已断开连接
#    连接特定的 DNS 后缀 . . . . . . . :