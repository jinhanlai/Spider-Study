#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 16:00
"""
#大鹏主页：http://www.renren.com/880151247/profile
#人人网登陆：http://www.renren.com/PLogin.do
from urllib import request

#不使用cookie
url="http://www.renren.com/880151247/profile"
header={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/76.0.3809.100 Safari/537.36",
    "Cookie":"anonymid=jzrw26cs-f8nsr6; Hm_lvt_1e59e639119e3bf348b864db2b258c57=1566792937; " \
             "Hm_lvt_4397070d9365caef87e72dc468269464=1566792938; depovince=GW; _r01_=1; JSESSIONID=abch_1qArvK5ketvqhsZw; ick_login=0bbb29ac-14ab-47cc-ad44-32bd144df57d; t=ef2b46a7e84203ea5a597492b44060684; societyguester=ef2b46a7e84203ea5a597492b44060684; id=972069274; xnsid=2dd4ea3b; ver=7.0; loginfrom=null; jebe_key=4bb7f80a-0cba-450a-ad24-cd0b9b3dea0e%7C68f9ad14e3e913f2b6c4b68878082a63%7C1566894136305%7C1%7C1566894138210; wp_fold=0; jebecookies=9d89e7aa-7928-4643-aebf-07d06426fb32|||||"

    }
req=request.Request(url=url,headers=header)
result=request.urlopen(req)

# print(result.read().decode('utf-8'))
with open('renren.html','w',encoding='utf-8') as fp:
    #注意write函数必须写入一个str数据类型
    #bytes->decode->str
    #str->encode->bytes
    fp.write(result.read().decode('utf-8'))

