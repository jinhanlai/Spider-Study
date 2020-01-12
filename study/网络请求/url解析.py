#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 13:00
"""
from urllib import parse

#url解析 urlparse()和urlsplit（）
url="https://pan.baidu.com/disk/home?#/all?path=%2F&vmode=list"
result=parse.urlparse(url)
result1=parse.urlsplit(url)#少了params这个参数
print(result)
print(result1)
print("scheme",result.scheme)