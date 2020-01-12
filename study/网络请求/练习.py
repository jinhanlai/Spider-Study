#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 13:45
"""
from urllib import parse,request

url='http://www.haha56.net/duanzi/201105/7939.html'
header={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Referer':'http://www.haha56.net/duanzi/201105/7940.html'
}
req=request.Request(url,headers=header,method="GET")
result=request.urlopen(req)
print(result.read())