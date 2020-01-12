# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/29 21:50
"""
import requests
import re

def parse_page(url):
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                     " (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }
    response=requests.get(url=url,headers=header)
    text=response.text
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)#是个列表包括所有的标题
    dynastics=re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tag=re.findall(r'div\sclass="contson".*?>(.*?)</div>', text, re.DOTALL)
    # print(author,content)
    contents=[]
    for content in content_tag:
        x=re.sub(r'<.*?>',"",content)
        contents.append(x.strip())
    # print(contents)
    poets=[]
    for values in zip(titles,dynastics,authors,contents):
        title,dynasty,author,content=values
        poet={
            'title':title,
            'dynastty':dynasty,
            'author':author,
            'content':content
        }
        poets.append(poet)
    for po in poets:
        print(po)
        print('='*30)

def spilder():
    ur="https://www.gushiwen.org/default_{}.aspx"
    for x in range(1,10):
        url=ur.format(x)
        parse_page(url)


if __name__ == '__main__':
    spilder()
