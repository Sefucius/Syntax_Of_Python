str='HelloPython,HelloJava,Hellophp'
target=input('请输入要统计的字符：')
print('{}在{}中一共出现了{}次'.format(target,str,str.upper().count(target)))