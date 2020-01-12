#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 21:43
"""
import requests
url="http://www.httpbin.org/ip"
proxy={
    "HTTP":"163.204.243.25:9999"
}

respons=requests.get(url,proxies=proxy)
print(respons.text)