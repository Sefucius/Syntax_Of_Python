#print()函数的完整的语法格式如下：
# print(value, ..., sep=' ', end='\n', file=None, flush=False)

a=100 # 变量a，值为100
b=50 # 变量b，值为50
print(90) # 输出90
print(a) # 输出变量a的值
print(b) # 输出变量b的值
print(a+b) # 输出变量a和b的和

print('北京欢迎你！') # 输出字符串
print("北京欢迎你！") # 输出字符串
print('''北京欢迎你！''') # 输出字符串
print("""北京欢迎你！""") # 输出字符串

#不换行一次输出多个数据
print(a,b,'北京欢迎你！')

#输出ASCII码对应的字符
print(chr(98)) # 输出b
print('b') # 输出b

#使用中文输出中文Unicode编码对应的字符
print(ord('北')) # 输出Unicode编码
print(chr(21271)) # 输出对应的字符
print(ord('京')) # 输出Unicode编码
print(chr(20140)) # 输出对应的字符

#将字符串写入文件
fp=open('note.txt','w') # 打开文件 w-->write
print('北京欢迎你！',file=fp) # 将北京欢迎你写入到文件
fp.close() # 关闭文件

#多个print()函数输出到同一行
print('北京',end='-->') 
print('欢迎你')

#连接两个字符串
print('北京'+'欢迎你') # 输出北京欢迎你
#print('北京'+100) # 错误，字符串不能和数字相连接