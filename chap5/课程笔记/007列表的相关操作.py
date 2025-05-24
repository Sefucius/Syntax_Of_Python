lst=['hello','world','python']

print('原列表',lst,id(lst))
# id(lst)  列表的内存地址

# 增加元素的操作
lst.append('sql')
print('添加元素后的列表',lst,id(lst))

# 使用insert(index,x)在指定的index位置插入元素x
lst.insert(1,100)
print('插入元素后的列表',lst,id(lst))

# 列表元素的删除操作
lst.remove('world')
print('删除元素后的列表',lst,id(lst))

# pop(index)删除并返回指定位置的元素，如果未指定位置则默认删除列表中最后一个元素
print(lst.pop(1))
print(lst)

'''
# 清除列表中的所有元素clear()
lst.clear()
print('清空元素后的列表',lst,id(lst))
'''

# 列表的反向
lst.reverse() # 不会产生新的列表，在原列表基础上进行操作
print('反向后的列表',lst,id(lst))

# 列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print('拷贝后的列表',new_lst,id(new_lst))

# 列表元素的修改操作
# 根据索引进行修改元素
lst[1]='mysql'
print(lst)