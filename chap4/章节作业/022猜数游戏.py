import random
rand= random.randint(1,100)
count=0
while 1:
    number=eval(input("在我心中有个数，1-100之间，请你猜一猜："))
    if number>rand:
        count+=1
        print("大了，宝宝再猜一次")
    elif number<rand:
        count+=1
        print("小了，宝宝再猜一次")
    else:
        count+=1
        print("猜对了\n还可以，宝宝一共猜了",count,"次")
        print("我爱你娜娜mua")
        break
