#用循环的方式打印一个爱心
for i in range(5):
    for j in range(5):
        if ((i==0 and j%2==1) 
        or (i==1 and j%2==0) 
        or (i-j==2) or (i+j==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
