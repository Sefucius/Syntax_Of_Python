def happy_birthday(name='张三',age=18):
   print(f'祝{name}生日快乐')
   print(f'{str(age)}岁生日快乐')

happy_birthday()
happy_birthday('李四')
happy_birthday('李四',20)
happy_birthday(age=20)

def fun(a,b=20):
   print(a,b)

""" 
 def fun(a=20,b)
    print(a,b) # 报错，因为b没有默认值，必须在a后面。 
"""