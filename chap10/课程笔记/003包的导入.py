import admin.my_admin as a # 包名.模块名
a.info()

print('-'*30)

from admin import my_admin as b # from 包名 import 模块名 as 别名
b.info()

print('-'*30)

from admin.my_admin import info  # from 包名.模块名 import 方法名
info()

print('-'*30)

from admin.my_admin import *  # from 包名.模块名 import *
print(name)

print('-'*30)

from admin.my_admin import info as c  # from 包名.模块名 import 方法名 as 别名
c()