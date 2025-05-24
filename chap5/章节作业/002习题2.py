lst1=[]
while True:
    temp=input('请输入商品编号和商品的名称进行商品入库，每次只能输入一件商品：')
    if temp=='q':
        break
    lst1.append(temp)
for index in range(len(lst1)):
    print(lst1[index])
lst2=[]
while True:
    temp=input('请输入要购买的商品编号：')
    if temp=='q':
        print('-'*30)
        break
    elif int(temp)-1000>=len(lst1):
        print('该商品不存在')
    else:
        lst2.append(lst1[int(temp)-1001])
        print('商品已成功添加到购物车')
lst2.reverse()
print('您购物车已选择的的商品为：')
for index in range(len(lst2)):
    print(lst2[index])