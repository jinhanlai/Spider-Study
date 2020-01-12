# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 11:04
"""
import requests
from lxml import etree

HEAD_URL = "https://dytt8.net"

#只抓取第一页所有的电影
url = "https://dytt8.net/html/gndy/dyzz/list_23_1.html"
header = {
    # 'Referer''Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36'
}
respons = requests.get(url=url, headers=header)
test = respons.text

#1.获取首页总的url
htmlElement = etree.HTML(test)
detai_url = htmlElement.xpath("//table[@class='tbspan']//a/@href")
detai_url=map(lambda x:HEAD_URL+x,detai_url)
# print(list(detai_url))

movies=[]
#2.进去每个url，并获得html
for de_url in detai_url:
    movie={}
    resp=requests.get(url=de_url,headers=header)
    tx=resp.content.decode('gbk')
    html=etree.HTML(tx)
    # print(etree.tostring(html,encoding='gbk').decode('gbk'))

    #3.获取每个url的详细信息
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title']=title

    zoom=html.xpath("//div[@id='Zoom']")[0]
    img=zoom.xpath(".//img/@src")
    cover = img[0]
    screenshot = img[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos=zoom.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info=info.replace("◎年　　代","").strip()
            movie["year"]=info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地","").strip()
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别","").strip()
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分","").strip()
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长","").strip()
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = info.replace("◎导　　演","").strip()
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = info.replace("◎主　　演", "").strip()
            actors=[info]
            for x in range(index+1,len(infos)):
                actor=infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors']=actors
        elif info.startswith("◎简　　介"):
            info = info.replace("◎简　　介","").strip()
            profile=""
            for x in range(index + 1, len(infos)):
                profile += infos[x].strip()
            movie["profile"] = profile
    download_url = zoom.xpath(".//table//a/@href")
    movie['download_url'] = download_url
    movies.append(movie)
    # print(download_url)
print(movies)