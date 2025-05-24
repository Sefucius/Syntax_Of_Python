import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()

# from ... import ...
from my_info import name
print(name)

from my_info import info
info()

from my_info import * # *是通配符，导入所有的变量和函数
print(name)
info()