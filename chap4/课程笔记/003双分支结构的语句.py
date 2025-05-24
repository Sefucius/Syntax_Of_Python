number=eval(input('请输入您的6位中奖号码:'))
# if...else语句
if number==987654 : #等值判断
    print('恭喜您中奖了')
else:
    print('很遗憾，您没有中奖')

print('----以上代码可以使用条件表达式进行简化----')

result='恭喜您中奖了' if number==987654 else '很遗憾，您没有中奖'
print(result)

print('恭喜您中奖了' if number==987654 else '很遗憾，您没有中奖')

# 条件表达式的语法格式为：表达式1 if 条件表达式 else 表达式2
# 如果条件表达式为真，则返回表达式1的值，否则返回表达式2的值