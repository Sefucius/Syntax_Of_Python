import requests
import re
url='https://detail.tmall.com/item.htm?detail_redpacket_pop=true&id=785024556621&ltk2=1745501078754islh18q4g5tvu4lwi4rl79&ns=1&priceTId=undefined&query=%E5%8D%8E%E4%B8%BA%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&skuId=5943239571905&spm=a21n57.1.hoverItem.2&utparam=%7B%22aplus_abtest%22%3A%22ba86fcded16c3d793764a4f0ede2e328%22%7D&xxc=ad_ztc'
# 爬虫打开浏览器上的网页
resp=requests.get(url) # 打开浏览器并打开网址
print(resp.text) # resp相应对象, 对象名.属性名 resp.text
# 设置一下编码格式
resp.encoding='utf-8'
print(resp.text)
reviews=re.findall('<div class="H7xLHMaqK8--content--_8e6708c" ([\u4e00-\u9fa5]*)</div>',resp.text)
# <link rel="stylesheet" type="text/css" href="//at.alicdn.com/t/a/font_4480420_sloucv8tyl.css">
# <div class="H7xLHMaqK8--content--_8e6708c" data-spm-anchor-id="pc_detail.29232929/evo365560b447259.202207.i1.68ae7dd6K1IWEh">电脑用了一段时间，非常轻便，办公使用非常方便，待电时间长，性价比很高，有国补更划算！</div>
# city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
lst=[]
for item in reviews:
    lst.append(item)
for item in lst:
    print(item) 
