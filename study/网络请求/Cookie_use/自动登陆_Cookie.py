#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 16:31
"""
#大鹏主页：http://www.renren.com/880151247/profile
#人人网登陆：http://www.renren.com/PLogin.do
from urllib import request,parse
from http.cookiejar import CookieJar

#1.登陆
#1.1创建一个cookiejar对象
cookierjar=CookieJar()
#1.2使用cookiejar创建一个httpCookieProcess对象
handler=request.HTTPCookieProcessor(cookierjar)
#1.3使用上一步创建的handler创建一个opener
opener=request.build_opener(handler)



#1.4使用opener发送登陆对的请求
headers={
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/76.0.3809.100 Safari/537.36"
}
data={
    'email':"15208213211",
    'password':"lailai5201314"
}
login_url="http://www.renren.com/PLogin.do"
req=request.Request(url=login_url,headers=headers,data=parse.urlencode(data).encode('utf-8'))
opener.open(req)



#2.访问个人主页
dap_url="http://www.renren.com/880151247/profile"
req=request.Request(url=dap_url,headers=headers)
result=opener.open(req)
with open('renren.html','w',encoding='utf-8') as fw:
    fw.write(result.read().decode('utf-8'))















