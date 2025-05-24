import openpyxl
# 打开工作簿
workbook = openpyxl.load_workbook('景区天气.xlsx')
# 选择要操作的工作表
sheet = workbook['景区天气']
# 表格数据为二位列表，先遍历的是行，后遍历的是列
lst=[] # 存储行数据
for row in sheet.rows:
    sublst=[] # 存储单元格数据
    for cell in row: # 遍历行中的每个单元格
        sublst.append(cell.value) # 将单元格的值添加到子列表中
    lst.append(sublst) # 将子列表添加到大列表中

for item in lst:
    print(item)