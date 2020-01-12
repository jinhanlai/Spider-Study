#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 17:27
"""
import requests

# #get方法
# url="https://www.baidu.com/s"
# params={
#     'wd':"中国"
# }
# header={
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
# response=requests.get(url=url,params=params,headers=header)
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))
# print(response.url)

#post方法
url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
data={
    'first':'true',
    'pn':'1',
    'kd':'python'
}
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                 " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}
prox={

}
respons=requests.post(url=url,headers=header,data=data,proxies=prox)
print(respons.json())
#verify=False可以处理不信任的ssh证书
# respons=requests.post(url=url,headers=header,data=data,proxies=prox,verify=False)


