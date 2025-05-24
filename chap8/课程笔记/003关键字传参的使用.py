def happy_birthday(name,age):
   print(f'祝{name}生日快乐')
   print(f'{str(age)}岁生日快乐')

happy_birthday(age=18,name='张三')
happy_birthday('张三',age=18) 
# 混合使用关键字传参和位置传参，
# 位置传参必须放在关键字传参前面，否则会报错。