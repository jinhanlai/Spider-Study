#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 17:05
"""
from urllib import request
from http.cookiejar import MozillaCookieJar

# #获得cookie信息
# cookiejar=MozillaCookieJar('cookie.txt')
# handle=request.HTTPCookieProcessor(cookiejar)
# opener=request.build_opener(handle)
#
# result=opener.open('http://www.httpbin.org/cookies/set?couse=asda')
# cookiejar.save(ignore_discard=True)

#本地加载cookie信息
cookiejar=MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)#ignore_discard=True会保存那些过时的cookie
handle=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handle)

result=opener.open('http://www.httpbin.org/cookies/set?couse=asda')
for cookie in cookiejar:
    print(cookie)

