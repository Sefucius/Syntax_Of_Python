class Instrument():
    def make_sound(self):
        pass
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')
class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

def play(Instrument):
    Instrument.make_sound()

erhu1=Erhu()
piano1=Piano()
violin1=Violin()
play(erhu1)
play(piano1)
play(violin1)