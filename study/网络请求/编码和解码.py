#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/27 12:44
"""
from urllib import request
from urllib import parse


params = {
    'from':'AUTO',
    'to':'AUTO'
}
data=parse.urlencode(params).encode('utf-8')
rep=request.urlopen(url="http://www.httpbin.org/post",data=data)
print(rep.read().decode('utf-8'))

#根据url下载图片
# rep=request.urlretrieve("http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg",'dowlod.jpg')

#urlencode()用法
# paramers={'name':"张三","age":15,'greet':'hello world'}
# result=parse.urlencode(paramers)
# print(result)

# url="https://www.baidu.com/s"
# parames={'wd':"刘德华"}
# qs=parse.urlencode(parames)
# url=url+"?"+qs
# req=request.urlopen(url)
# print(req.read())

# #parse_qs()解码的使用
# paramers={'name':"张三","age":15,'greet':'hello world'}
# qs=parse.urlencode(paramers)
# print(qs)
# result=parse.parse_qs(qs)
# print(result)
