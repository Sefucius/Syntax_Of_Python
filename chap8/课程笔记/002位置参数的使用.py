def happy_birthday(name,age):
   print(f'祝{name}生日快乐')
   print(f'{str(age)}岁生日快乐')

# 调用函数
# happy_birthday('张三')  #报错，缺少一个位置参数
# 顺序也要正确
happy_birthday('张三',18)