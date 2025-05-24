# 第一段代码
lst=[11,22,33,44]
print(lst[4]) # 报错,因为索引超出了列表的范围

# 第二段代码
lst=[]
# lst=append('A','B','C') # 报错,append()方法没有返回值
lst.append('A')
lst.append('B')
lst.append('C')
print(lst) # 输出['A','B','C']