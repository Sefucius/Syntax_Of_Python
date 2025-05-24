while 1:
    print('----- 模拟10086查询功能 -----')
    print('1.查看当前余额')
    print('2.查看当前剩余流量')
    print('3.查看当前剩余通话时长')
    print('0.退出系统')
    key = input('请输入您要执行的操作:')
    if key == '1':
        print('当前余额为:234.5元')
        temp=input('还继续操作吗？y/n')
        if temp=='y':
            continue
        else:
            print('程序退出，感谢您的使用！')
            break
    elif key == '2':
        print('当前剩余流量为:4GB')
        temp=input('还继续操作吗？y/n')
        if temp=='y':
            continue
        else:
            print('程序退出，感谢您的使用！')
            break
    elif key == '3':
        print('当前剩余通话时长为:50小时')
        temp=input('还继续操作吗？y/n')
        if temp=='y':
            continue
        else:
            print('程序退出，感谢您的使用！')
            break
    elif key == '0':
        print('感谢使用,欢迎下次再来!')
        break
    else:
        print('输入有误,请重新输入!')
