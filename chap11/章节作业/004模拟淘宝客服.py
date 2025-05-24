import os
import os.path as op
import logging

def get_answer(question):
    while True:
        if (question!='bye') and (('订单' or '物流' or '账户' or '支付' ) not in question):
            question=input('小蜜不知道您说的是什么，您还可以问一问关于订单、物流、账户、支付等问题，退出请输入bye：')
            get_answer(question)
            break
        elif (question=='bye'):
            print('小主再见')
            break
        else:
            with open('reply.txt', 'r', encoding='utf-8') as f:
            # 逐行读取文件内容
                for line in f:
                    # 将每行内容按'|'分割成关键词和回复
                    keyword = line.split('|')[0]
                    reply = line.split('|')[1]
                    # 如果问题中包含关键词，返回对应的回复
                    if keyword in question:
                        print(reply)
            question=input('小主，您还可以问一些关于订单、物流、账户、支付等问题，退出请输入bye：') 
            get_answer(question)
            break        
    
# 主函数
if __name__ == '__main__':
    os.chdir(r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\章节作业\taobao')
    question=input('Hi，小主您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧：')
    get_answer(question)