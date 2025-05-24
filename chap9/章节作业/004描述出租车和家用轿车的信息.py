class Car():
    def __init__(self,model,licence):
        self.model=model
        self.licence=licence
    def run(self):
        print('启动')
    def stop(self):
        print('停止')

class Taxi(Car):
    def __init__(self,model,licence,company):
        super().__init__(model,licence)
        self.company=company
    def run(self):
        print('乘客您好！')
        print(f'我是{self.company}的，我的车牌号是{self.licence}，您要去哪里？')
    def stop(self):
        print('目的地到了，请您付款下车，欢迎下次乘坐！')
        print('-'*30)
    
class Sedan(Car):
    def __init__(self,model,licence,name):
        super().__init__(model,licence)
        self.name=name
    def run(self):
        print(f'我是{self.name}，我的汽车我做主')
    def stop(self):
        print('目的地到了，我们去玩吧！')
        print('-'*30)

taxi1=Taxi('宝马','京A88888','途安')
taxi1.run()
taxi1.stop()

sedan1=Sedan('奔驰','京B99999','娜娜')
sedan1.run()
sedan1.stop()

sedan2=Sedan('宝马','京C00000','浩浩')
sedan2.run()
sedan2.stop()

