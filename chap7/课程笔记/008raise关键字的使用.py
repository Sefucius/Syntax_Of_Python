try:
    gender=input("请输入你的性别：")
    if gender=="男"and gender!="女":
        raise Exception("性别只能是男或者女")
    else:
        print("您的性别是:",gender)
except Exception as e:
    print(e)