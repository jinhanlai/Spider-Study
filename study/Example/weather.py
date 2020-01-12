# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/29 13:24
"""
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from  pyecharts import  options as opts

ALL_city=[]
def parse_url(url):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) A"
                      "ppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        'Referer': "http://www.weather.com.cn/textFC/xn.shtml",
        'Host': "www.weather.com.cn"
    }
    response = requests.get(url=url, headers=header)
    text = response.content.decode('utf-8')
    # print(text)
    # html5lib
    soup = BeautifulSoup(text, "html5lib")
    # soup=BeautifulSoup(text,"lxml")
    conMidtab = soup.find('div', attrs={'class': 'conMidtab'})  # 找到第一个class=conMidtab
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city = list(tds[0].stripped_strings)[0]
            if index == 0:
                # print("=" * 25, "省份：", city, "=" * 25)
                city = list(tds[1].stripped_strings)[0]
            min_tp = list(tds[-2].stripped_strings)[0]
            # print({'city': city, "min_temperate": int(min_tp)})
            ALL_city.append({'city': city, "min_temperate": int(min_tp)})



def spilder():
    # url="http://www.weather.com.cn/textFC/hb.shtml"
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_url(url)

    ALL_city.sort(key=lambda x:x['min_temperate'])
    data=ALL_city[0:10]
    # print(data)
    citys=list(map(lambda x:x['city'],data))
    temps=list(map(lambda x:x['min_temperate'],data))
    chart=(
        Bar()
        .add_xaxis(citys)
        .add_yaxis("温度",temps)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国天气最低气温排行"))
           )
    chart.render("temperature.html")


    # print(ALL_city)

if __name__ == '__main__':
    spilder()
