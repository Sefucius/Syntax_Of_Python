str1 = input("请输入一个字符串：")
def fun(s):
    sum = 0
    lst = []
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
            lst.append(int(s[i]))
    return lst,sum
result = fun(str1)
print(f'提取的数字列表为:{result[0]}')
print(f'累加和为:{result[1]}')