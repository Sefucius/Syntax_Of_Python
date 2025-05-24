from PIL import Image
# 加载图片
img = Image.open("baidu.jpg")
print(type(img),img)
# 提取RGB图像的颜色通道，返回结果是图像的副本
r,g,b = img.split()
# print(r)
# print(g)
# print(b)
# 合并通道
img2 = Image.merge(mode='RGB',bands=(b,g,r))
img2.show()
img2.save("baidu2.jpg")