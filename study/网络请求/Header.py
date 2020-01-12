# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 13:12
"""
from urllib import request,parse

# url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
# rep=request.urlopen(url)
# print(rep.read())
url="https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false"

data={
    'first':'true',
    'pn':1,
    'kd':'python'
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E6%88%90%E9%83%BD'
}

rep = request.Request(url, headers=headers
                      ,data=parse.urlencode(data).encode('utf-8'),method='POST')
result = request.urlopen(rep)
print(result.read().decode('utf-8'))
