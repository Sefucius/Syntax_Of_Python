lst=[54,56,77,4,567,34]

# 排序
asc_lst=sorted(lst) # 升序
desc_lst=sorted(lst,reverse=True) # 降序
print('原列表：',lst)
print('升序：',asc_lst)
print('降序：',desc_lst)

# 反转
new_lst=reversed(lst)
print(type(new_lst)) # 反转后返回的是一个迭代器
print(list(new_lst))

# zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj)) # 转换为迭代器
# print(list(zipobj))

# enumerate
enum=enumerate(y,start=1) # 从1开始
print(type(enum)) # 转换为迭代器
print(tuple(enum))

# all
lst2=[10,20,'',30]
print(all(lst2)) # False
print(all(lst)) # True

# any
print(any(lst2)) # True
print(any(lst)) # True

# next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))


def fun(num):
    return num%2==1 

# filter
filterobj=filter(fun,range(10)) # 过滤
print(type(filterobj)) # 转换为迭代器
print(list(filterobj)) # [1, 3, 5, 7, 9]

def upper(x):
    return x.upper()

# map
new_lst2=['hello','world','python']
obj2=map(upper,new_lst2) # 映射
print(list(obj2)) # ['HELLO', 'WORLD', 'PYTHON']