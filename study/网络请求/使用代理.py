#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 15:43
"""
from urllib import request

url="http://www.httpbin.org/ip"
#1.使用ProxyHandler，传入代理构建一个handler
handler=request.ProxyHandler({"Http":"117.87.176.114:9000"})
#2.使用上面创建的handler构建一个opener
opener=request.build_opener(handler)
#3.使用opener去构建一个请求
rep=opener.open(url)
print(rep.read())