# 这个文件需要在单独的terminal窗口中运行
import socket 

# 创建一个socket对象
client_socket = socket.socket()

# ip地址和主机端口
ip='172.27.96.42'
port=8888
client_socket.connect((ip,port))
print('------------客户端已连接到服务器------------')

# 发送数据
data='祝你天天开心'
client_socket.send(data.encode('utf-8'))
print('------------客户端已发送数据------------')

# 关闭
client_socket.close()
print('------------发送完毕------------')
