def change_case(s):
    new_str = []
    for i in s:
        if i.isupper():
            new_str.append(i.lower())
        else:
            new_str.append(i.upper())
    return ''.join(new_str)

str1 = input('请输入一个字符串:')
print(change_case(str1))