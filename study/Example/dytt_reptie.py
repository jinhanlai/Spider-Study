#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 14:09
"""
import requests
from lxml import etree

HEAD_URL = "https://dytt8.net"
PG_URL= "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
HEADER={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
}
def get_detail_url(url):
    respons = requests.get(url=url, headers=HEADER)
    test = respons.text
    # 1.获取每页总的url
    htmlElement = etree.HTML(test)
    detail_urls = htmlElement.xpath("//table[@class='tbspan']//a/@href")
    detai_urls = map(lambda x: HEAD_URL + x, detail_urls)
    return detai_urls

def get_detail_page(url):
    """
    获取每个url的详细信息
    """
    movie = {}
    resp = requests.get(url=url, headers=HEADER)
    tx = resp.content.decode('gbk')
    html = etree.HTML(tx)
    # print(etree.tostring(html,encoding='gbk').decode('gbk'))

    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoom = html.xpath("//div[@id='Zoom']")[0]
    img = zoom.xpath(".//img/@src")
    cover = img[0]
    screenshot = img[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos = zoom.xpath(".//text()")
    for index, info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代", "").strip()
            movie["year"] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长", "").strip()
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = info.replace("◎导　　演", "").strip()
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = info.replace("◎主　　演", "").strip()
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            # info = info.replace("◎简　　介", "").strip()
            profile = ""
            for x in range(index + 1, len(infos)):
                profile += infos[x].strip()
            movie["profile"] = profile
    download_url = zoom.xpath(".//table//a/@href")
    movie['download_url'] = download_url
    return movie
def spider():
    movies=[]
    #爬取7页的url
    for x in range(1,3):
        url=PG_URL.format(x)
        detail_urls=get_detail_url(url)
        for d_url in detail_urls:
            movie=get_detail_page(d_url)
            movies.append(movie)
    print(movies)
if __name__ == '__main__':
    spider()

