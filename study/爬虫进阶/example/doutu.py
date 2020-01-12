# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/31 13:42
"""
import requests
import re
import os


def parse_page(url):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    response = requests.get(url=url, headers=header)
    text = response.text
    # print(text)
    img_url = re.findall('<img\sreferrerpolicy="no-referrer".*?data-original="(.*?)".*?>', text, re.DOTALL)
    alt = re.findall('<img\sreferrerpolicy="no-referrer".*?alt="(.*?)".*?>', text, re.DOTALL)
    houzui = list(map(lambda x: os.path.splitext(x)[1], img_url))  # 获取文件后缀名
    filename = [(alt[i] + houzui[i]) for i in range(0, len(alt))]

    for i in range(0, len(filename)):
        res=requests.get(img_url[i])
        # print(res.content)
        with open('images/' + filename[i],'wb') as f:
            f.write(res.content)


def spilder():
    url = "http://www.doutula.com/photo/list/?page={}"
    for i in range(1,4):
        parse_page(url.format(i))


if __name__ == '__main__':
    spilder()
