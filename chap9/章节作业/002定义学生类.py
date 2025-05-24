class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
    def info(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，分数：{self.score}")

lst=[]
for i in range(5):
    temp_str = input(f"请输入第{i+1}位学生的信息及成绩：")
    temp_list = temp_str.split("#")
    temp_student = Student(temp_list[0], temp_list[1], temp_list[2], temp_list[3])
    lst.append(temp_student)

for i in range(len(lst)):
    lst[i].info()

    