import wx
from socket import socket,AF_INET,SOCK_STREAM
import threading
class HwhServer(wx.Frame):

    def __init__(self, name=None):
        wx.Frame.__init__(self, None, id=1002 ,title='hwh服务器端界面' ,pos=wx.DefaultPosition , size=(400,450))
        # if name:
        #     print(f"接收到的名称: {name}")
        # 创建面板
        panel = wx.Panel(self)
        # 面板上放一个盒
        box=wx.BoxSizer(wx.VERTICAL) # 垂直方向布局
        # 可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局 

        start_server_btn=wx.Button(panel,size=(133,40),label='启动服务')
        record_btn=wx.Button(panel,size=(133,40),label='保存聊天记录')
        stop_server_btn=wx.Button(panel,size=(133,40),label='停止服务')

        # 按到可伸缩的网格布局当中
        fgz1.Add(start_server_btn,1,wx.TOP)
        fgz1.Add(record_btn,1,wx.TOP)
        fgz1.Add(stop_server_btn,1,wx.TOP)

        # 把可伸缩的网格布局添加到盒当中
        box.Add(fgz1,1,wx.ALIGN_CENTER)

        # 只读的多行文本框
        # 只读文本框，显示聊天内容
        self.show_text = wx.TextCtrl(panel, size=(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTER)

        # 把盒添加到面板当中
        panel.SetSizer(box)
        '''------以上都是界面的绘制代码------'''
    
        '''------服务器功能实现的必要属性------'''
        self.ison=False # 存储服务器的启动状态，默认是关闭
        # 服务器端所绑定的IP地址和端口号
        self.host_port=('',8888) # 空字符串表示本机的所有IP
        # 创建socket对象
        self.server_socket=socket(AF_INET,SOCK_STREAM)
        # 绑定IP地址和端口号
        self.server_socket.bind(self.host_port)
        # 监听
        self.server_socket.listen(5) 
        # 创建一个字典，存储与客户端对话的会话线程
        self.session_thread_dict={} # key-value {客户端的名称key:会话线程value}
        # 当鼠标点击服务器“启动服务”按钮时，要执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn)

    def start_server(self,event):
        # 判断服务器是否已经启动，没启动时才启动
        if self.ison==False:
            # 启动服务器
            self.ison=True
            # 创建主线程对象，用于接收客户端连接请求
            main_thread=threading.Thread(target=self.do_work)
            # 设置线程为守护线程，父线程执行结束（窗体界面），子线程也会结束
            main_thread.daemon=True
            # 启动主线程
            main_thread.start()

    def do_work(self):
        # 判断ison的值，为True时，执行下面的代码
        while self.ison:
            # 接收客户端连接请求，返回值是一个元组，包含客户端的socket对象和客户端的IP地址和端口号
            client_socket,client_addr=self.server_socket.accept()
            # 接收客户端发送的名称
            user_name=client_socket.recv(1024).decode('utf-8')
            # 创建一个会话线程的对象
            session_thread=SesstionThread(client_socket,user_name,self)
            # 存储到字典中
            self.session_thread_dict[user_name]=session_thread
            # 启动会话线程
            session_thread.start()
        # 当self.ison==False时，关闭socket对象
        self.server_socket.close()


# 服务器端会话线程类        
class SesstionThread(threading.Thread):
    def __init__(self,client_socket,user_name):
        super().__init__() # 调用父类的构造函数
        self.client_socket=client_socket # 客户端的socket对象
        self.user_name=user_name # 客户端的名称
        self.server=server # 服务器端的对象
        self.ison=True # 会话线程的启动状态，默认是启动的



    def run(self) -> None:
        print(f'客户端{self.user_name}和服务器连接成功，服务器启动一个会话线程')
        while self.ison:
            # 接收客户端发送的消息
            recv_data=self.client_socket.recv(1024).decode('utf-8')
            # 当接收到的消息是'bye'时，结束会话
            if recv_data=='bye':
                self.ison=False
            else:
                # 其它聊天信息显示给所有的客户端，包含服务器也显示
                pass
        # 关闭客户端的socket对象
        self.client_socket.close()

if __name__=='__main__':
    # 初始化APP
    app=wx.App()
    # 创建自己的客户端界面对象
    server = HwhServer('Python浩浩')
    server.Show() 

    # 循环刷新显示，修正方法名大小写
    app.MainLoop()

