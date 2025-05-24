a=int(input("请输入第一条边："))
b=int(input("请输入第二条边："))
c=int(input("请输入第三条边："))
try:
    if a+b>c and a+c>b and b+c>a:
        print("三角形的边长为:a={},b={},c={}".format(a,b,c))
    else:
        raise Exception("不能构成三角形")
except Exception as e:
    print('a={},b={},c={},{}'.format(a,b,c,e))
except ValueError:
    print(ValueError)
  