import pdfplumber
# 打开PDF文件
with pdfplumber.open('小学数学.pdf') as pdf:
    # 遍历每一页
    for i in pdf.pages:
        print(i.extract_text()) # extract_text()方法用于提取文本内容
        print(f'------------第{i.page_number}页结束------------')
