from prettytable import PrettyTable

# 创建表格对象
table = PrettyTable()

# 添加列
table.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]

# 添加行数据
for i in range(6):
    table.add_row([f'第{i+1}行', '有票', '有票', '有票', '有票', '有票'])

# 打印表格
print(table)
seat=input('请输入选择的座席，如4,3表示第4行第3列：')
seat=seat.split(',')
print(seat)
row=int(seat[0])-1
col=int(seat[1])
print(table.rows)
print(table._rows)
# 检查行和列的有效性
if row < 0 or row >= len(table.rows):
    print("行号无效！")
elif col < 1 or col > 5:  # 列号应为1-5，对应索引1-5
    print("列号无效！")
else:
    # 检查座位状态并修改
    if table.rows[row][col] == '有票':
        table.rows[row][col] = '已售'  # 修改座位状态为已售
        print('购买成功！')
    else:
        print('该座位已售出！')

print(table)