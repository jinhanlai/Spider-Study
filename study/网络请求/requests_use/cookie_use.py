#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 22:04
"""
import requests


dapenurl="http://www.renren.com/880151247/profile"
renren="http://www.renren.com/PLogin.do"

header={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/76.0.3809.100 Safari/537.36",
    }
data={
    'email':"15208213211",
    'password':"lailai5201314"
}
session=requests.Session()

session.post(url=renren,data=data,headers=header)

response=session.get(url=dapenurl)

with open("renren.html","w",encoding='utf-8') as fp:
    fp.write(response.text)












