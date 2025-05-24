def calc(a,b):
    return a+b

print(calc(1,2))

# 匿名函数
calc2 = lambda a,b:a+b
print(calc2(1,2))
print(type(calc2))

lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

for i in range(len(lst)):
    result=lambda x:x[i]
    print(result(lst))


student_score=[
                {'name':'陈梅梅','score':98}
               ,{'name':'王大A','score':93}
               ,{'name':'王大B','score':92}
               ,{'name':'王大C','score':91}
               ]

student_score.sort(key=lambda x:x['score'],reverse=True)
# reverse=True 降序
print(student_score)