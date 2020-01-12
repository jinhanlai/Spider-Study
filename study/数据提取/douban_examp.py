#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 10:42
"""
import requests
from lxml import etree

url="https://movie.douban.com/cinema/nowplaying/chengdu/"
headler={
    'Rerfer':"https://movie.douban.com/",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                 " (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
response=requests.get(url=url,headers=headler)
txt=response.text
htmlElement=etree.HTML(txt)
# print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))
movies=[]
uls=htmlElement.xpath("//ul[@class='lists']")[0]
lis=uls.xpath("./li")
for li in lis:
    title=li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    direcotr = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    post=li.xpath(".//img/@src")
    movie={
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'direcotr':direcotr,
        'actors':actors,
        'post':post
    }
    movies.append(movie)
print(movies)

























