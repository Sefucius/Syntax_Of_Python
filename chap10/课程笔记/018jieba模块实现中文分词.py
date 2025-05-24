import jieba
# 读取文件
with open('华为笔记本电脑评论.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# print(text)
# 分词
lst=jieba.lcut(text)
# print(lst)

# 去重操作
set1=set(lst) # 集合的去重
# print(set1)
# 统计词频
dic={} # 空字典   key键：词语  value值：词频
for item in set1:
    if len(item)>=2:
        dic[item]=lst.count(item)
# print(dic)
new_lst=[]
for item in dic:
    new_lst.append([item,dic[item]]) 
print(new_lst)
# 排序
new_lst.sort(key=lambda x:x[1],reverse=True) # 降序
print('-'*50)
print('高频词：',new_lst[0:11])