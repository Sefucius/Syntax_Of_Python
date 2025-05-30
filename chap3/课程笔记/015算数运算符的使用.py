# 运算符优先级如下：
# ** 指数 (最高优先级)
# ~ + - 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % // 乘，除，取模和取整除
# + - 加法减法
# >> << 右移，左移运算符
# & 位 'AND'
# ^ | 位运算符
# <= < > >= 比较运算符
# <> == != 等于运算符
# = %= /= //= -= += *= **= 赋值运算符
# is is not 身份运算符
# in not in 成员运算符
# not or and 逻辑运算符


print('加法',1+1)
print('减法',1-1)
print('乘法',2*2)
print('除法',3/2)
print('取余',3%2)
print('整除',3//2)
print('幂',2**3) # 2的3次方
print('开方',4**0.5) # 4的0.5次方
print('四舍五入',round(3.1415926,2)) # 保留两位小数
print('绝对值',abs(-1)) # 取绝对值
print('最大值',max(1,2,3)) # 取最大值
print('最小值',min(1,2,3)) # 取最小值
print('求和',sum([1,2,3])) # 求和
print('平均值',sum([1,2,3])/len([1,2,3])) # 平均值
print('整数转换',int(1.1)) # 转换为整数
print('浮点数转换',float(1)) # 转换为浮点数
print('字符串转换',str(1)) # 转换为字符串
print('布尔值转换',bool(1)) # 转换为布尔值
print('复数',complex(1,2)) # 复数
