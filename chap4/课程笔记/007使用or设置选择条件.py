score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('成绩输入错误！')
else:
    print('您的成绩为：',score)