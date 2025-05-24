fuck = open('practice1.txt', 'w')  # 打开文件 w-->write
print('人生苦短，我用Python', file=fuck)  # 写入文件
fuck.close()  # 关闭文件