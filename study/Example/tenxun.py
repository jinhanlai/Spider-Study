#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 21:00
"""
import requests
from lxml import etree

url="https://careers.tencent.com/search.html?index={}&keyword=python"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                 " (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Referer':'https://careers.tencent.com/'
}
def get_url(url):
    respons=requests.get(url=url,headers=header)
    test=respons.text
    print(test)
    htmlElement=etree.HTML(test)
    detail_urls = htmlElement.xpath("//div[@class='recruit-list']/a/@href")
    print(detail_urls)
    # detai_urls = map(lambda x: HEAD_URL + x, detail_urls)
    return detail_urls

def spider():
    for i in range(1,5):
        ur = url.format(i)
        # print(ur)
        det_urls=get_url("http://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10")
        print(det_urls)
        break
if __name__ == '__main__':
    spider()
