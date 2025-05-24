import weather
import openpyxl
html = weather.get_html() #获取网页
lst = weather.parse_html(html) #解析网页
# 创建excel工作簿
workbook = openpyxl.Workbook() 
# 在excel中创建工作表
sheet = workbook.create_sheet('景区天气')
# 向工作表中添加数据
for item in lst:
    sheet.append(item) # 一次添加一行

workbook.save('景区天气.xlsx') # 保存excel文件