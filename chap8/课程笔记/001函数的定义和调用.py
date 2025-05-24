def get_sum(num): # num为形式参数
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1~{num}之间的累加和为：{s}')
    return s
# 调用函数
# 10、100为实际参数
get_sum(10) # 1~10之间的累加和为：55
get_sum(100) # 1~100之间的累加和为：5050
print(get_sum(10)) # 1~10之间的累加和为：55  55