from datetime import datetime # 从datetime模块中导入datetime类
import time
import os
import random

def sign(dic):
    print('请注册账号')
    username = input('请输入用户名：')
    password = input('请输入密码：')
    dic[username]=password
    print('注册成功！')

def login(dic): 
    username = input('请输入用户名：')
    password = input('请输入密码：') 
    if dic.get(username) and password == dic.get(username): 
        print('登录成功！') 
        # 修改当前的工作路径
        os.chdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\章节作业\AdminFolder')
        # 记录登录时间
        with open('log.txt', 'a', encoding='utf-8') as f: 
            nowdt=datetime.now()
            nowdt_str=nowdt.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'用户名:{username},登录时间:{nowdt_str}\n') # 写入用户名和登录时间
        while True:
            print('输入提示数字,执行相应操作:0.退出 1.查看登录日志')
            num = int(input('输入操作数字：'))
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                # 修改当前的工作路径
                os.chdir('E:\Microsoft Visual Studio\Project\Python_learning\chap11\章节作业\AdminFolder')
                with open('log.txt', 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print('输入错误,请重新输入')
    else:
        print('用户名或密码错误！') 


# 主函数
if __name__ == '__main__':
    # 定义一个字典，用于存储用户信息
    dic = {'hwh':'142857'}
#   sign(dic)
    login(dic)

