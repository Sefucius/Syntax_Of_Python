import requests
import re

# 定义函数
def get_html():
    url='https://www.weather.com.cn/weather1d/101310201.shtml'
    # 爬虫打开浏览器上的网页
    resp=requests.get(url) # 打开浏览器并打开网址
    # 设置一下编码格式
    resp.encoding='utf-8'
    return resp.text

def parse_html(html_str):
    # 解析网页
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd=re.findall('<span class="wd">(.*)</span>',html_str)
    zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str)
    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst


    
""" 
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">25/32℃</span>
<span class="zs">适宜</span> 
"""