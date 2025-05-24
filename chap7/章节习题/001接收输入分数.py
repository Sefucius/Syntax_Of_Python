score=int(input('请输入分数：'))
try:
    score=float(score)
    if score>=0 and score<=100:
        print('分数为:{}'.format(int(score)))
    if not (score>=0 and score<=100):
        raise Exception(int(score))
except Exception as e:
    print('输入分数为：{}，不正确'.format(e))
except ValueError:
    print(ValueError)