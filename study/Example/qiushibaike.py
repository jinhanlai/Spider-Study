# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/29 23:04
"""
import requests
import re

def delet_strip(conts_flag):
    conts=[]
    for x in conts_flag:
        cont=x.strip()
        conts.append(cont)
    return conts

def parse_page(url):
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        'Referer':"https://www.qiushibaike.com/",
        'Host':"www.qiushibaike.com"
    }
    respones=requests.get(url=url,headers=header)
    text=respones.text
    print(text)
    author_flag=re.findall('<div\sclass="author clearfix">.*?<a.*?>.*?<h2>(.*?)</h2>',text,re.DOTALL)
    authors=delet_strip(author_flag)

    content=re.findall('<div\sclass="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    contents=delet_strip(content)
    # print(contents)

    alls=[]
    for values in zip(authors,contents):
        author,content=values
        all={
            'author':author,
            'content':content
        }
        alls.append(all)
    for x in alls:
        print(x)
        print('=='*30)

def spilder():
    # url = "https://www.qiushibaike.com/text/page/1/"
    ur = "https://www.qiushibaike.com/text/page/{}/"
    for i in range(1,11):
        url=ur.format(i)
        parse_page(url)


if __name__ == '__main__':
    spilder()
