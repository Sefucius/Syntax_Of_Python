try:
    num1=int(input("请输入第一个整数："))
    num2=int(input("请输入第二个整数："))
    result=num1/num2
except ZeroDivisionError: 
    print("除数为0")
except ValueError: 
    print("输入的不是整数")
except BaseException:
    pass
else:
    print("两个整数相除的结果为：",result)
finally:
    print("程序结束")