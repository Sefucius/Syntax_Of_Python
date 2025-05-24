answer=input('请问，您喝酒了吗？')
if answer=='yes':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('构不成酒驾，祝您一路平安！')
    elif proof<80:
        print('构成酒驾，罚款2000元，记12分，吊销驾照！')
    else:
        print('构成醉驾，罚款2000元，记12分，吊销驾照！')
else:
    print('祝您一路平安！')