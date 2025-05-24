note=set()
while True:
    note.add(input('请输入第'+str(len(note)+1)+'位好友的姓名与手机号码：'))
    if len(note)==5:
        break
for i in note:
    print(i)    