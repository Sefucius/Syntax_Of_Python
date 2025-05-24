def in_(a,b):
    for i in b:
        if i==a:
            return True
    return False
""" 
if in_(input('请输入您要判断的字符串:'),[1,'hello',3,4,5]):
    print('存在')
else:
    print('不存在') 
"""
print('存在' if in_(input('请输入您要判断的字符串:'),[1,'hello',3,4,5]) else '不存在')
