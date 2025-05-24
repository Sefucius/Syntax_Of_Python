height_father = input('请输入爸爸的身高：')
height_mother = input('请输入妈妈的身高：')
height_father = float(height_father)
height_mother = float(height_mother)
height_son = (height_father + height_mother) * 0.54
print('预测儿子的身高为：', height_son)