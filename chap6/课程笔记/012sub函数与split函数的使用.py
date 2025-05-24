import re
pattern='黑客|破解|反爬'
s='我想学习Python，像破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://www.bilibili.com/video/BV1wD4y1o7AS?spm_id_from=333.788.player.switch&vd_source=1bc5a978020cf7dc2fc24254c7fcc6ce&p=74'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)