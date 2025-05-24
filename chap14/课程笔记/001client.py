# coding: utf-8
import wx
from socket import socket,AF_INET,SOCK_STREAM
class hwhClient(wx.Frame):
    def __init__(self,client_name):
        # 调用父类的初始化方法
        # None:没有父级窗口
        # id表示当前窗口的一个编号
        # pos:窗体的打开位置
        # size:窗体的大小
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端页面',pos=wx.DefaultPosition,size=(400,450))
        # 创建面板对象
        pl=wx.Panel(self)
        # 在面板中放上盒子
        box=wx.BoxSizer(wx.VERTICAL) # 垂直方向布局
        # 可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局 

        # 创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        dis_conn_btn=wx.Button(pl,size=(200,40),label='断开')

        # 把两个按钮放到可伸缩的网格布局中
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT) 
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        # (可伸缩的网格布局)添加到box中
        box.Add(fgz1,1,wx.ALIGN_CENTER) 

        # 只读文本框,显示聊天内容
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTER)

        # 创建聊天内容的文本框
        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.chat_text,1,wx.ALIGN_CENTER)
        # 可伸缩的网格布局
        fgz2=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局
        # 创建两个按钮
        reset_btn=wx.Button(pl,size=(200,40),label='重置')
        send_btn=wx.Button(pl,size=(200,40),label='发送')
        # 把两个按钮放到可伸缩的网格布局中
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)
        # (可伸缩的网格布局)添加到box中
        box.Add(fgz2,1,wx.ALIGN_CENTER)
        # 把box添加到面板中
        pl.SetSizer(box)

        '''---以上代码是客户端界面的绘制---'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn) # 绑定连接按钮的事件
        # 实例属性的设置
        self.client_name=client_name
        self.isConnected=False # 表示当前客户端是否连接上了服务器
        self.Client_socket=None # 设置客户端的socket对象为空


    def connect_to_server(self,event): # 连接服务器的方法
        print(f'客户端{self.client_name}连接服务器成功')
        # 如果客户端没有连接服务器，则开始连接
        if not self.isConnected: # 等价于self.isConnected==False
            # TCP编程的步骤
            server_host_port=('172.27.96.42',8888)
            # 创建socket对象
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            # 发送连接请求
            self.client_socket.connect(server_host_port)
            # 只要连接成功，发送连接成功的消息
            self.client_socket.send(self.client_name.encode('utf-8'))
            # 启动一个线程，客户端线程与服务器会话线程进行会话
            client_thread=wx.Thread(target=self.recv_data)
            # 设置成守护线程，窗体关闭，子线程也结束了
            client_thread.daemon=True
            # 修改一下连接状态
            self.isConnected=True
            # 启动线程
            client_thread.start()
    
    
    def recv_data(self):
        pass        



if __name__=='__main__':
    # 初始化APP
    app=wx.App()
    # 创建自己的客户端界面对象
    client=hwhClient('hwh')
    # 显示
    client.Show()

    # 进入主事件循环
    app.MainLoop()