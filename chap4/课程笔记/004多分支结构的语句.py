score=eval(input('请输入你的成绩：'))
if score<0 or score>100:
    print('成绩有误！')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')        
