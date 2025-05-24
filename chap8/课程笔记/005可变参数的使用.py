# 个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

fun(10,20,30,40)
fun(10)
fun()
fun([10,20,30,40])

fun(*[10,20,30,40]) 
# 拆包，把列表中的元素作为位置参数传递给函数


# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'----->',value)

fun2(name='张三',age=18,gender='男')

d={'name':'李四','age':20,'gender':'人妖' }
fun2(**d)