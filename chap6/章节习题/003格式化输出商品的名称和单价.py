lst=[['编号','名称','品牌','单价']
,['01','电风扇','美的','500']
,['02','洗衣机','TCL','1000']
,['03','微波炉','老板','400']]
for row in lst:
    for item in row:
        print(item,end='\t')
    print()
print('-'*30)
for i in range(1,len(lst)):
    lst[i][0]='{}{}'.format('0000',lst[i][0])
    lst[i][3]='{}{}{}'.format('￥',lst[i][3],'.00')
for row in lst:
    for item in row:
        print(item,end='\t')
    print()
