#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 9:07
"""
from lxml import etree
text="""<head>
    <meta name="Description" content="人人网 校内是一个真实的社交网络，联络你和你周围的朋友。 加入人人网校内你可以:联络朋友，了解他们的最新动态；和朋友分享相片、音乐和电影；找到老同学，结识新朋友；用照片和日志记录生活,展示自我。"/>
    <meta name="Keywords" content="Xiaonei,Renren,校内,大学,同学,同事,白领,个人主页,博客,相册,群组,社区,交友,聊天,音乐,视频,校园,人人,人人网"/>
    <title>人人网 - 大鹏董成鹏</title>
    <meta charset="utf-8"/>
<link rel="shortcut icon" type="image/x-icon" href="http://a.xnimg.cn/favicon-rr.ico?ver=3" />
<link rel="apple-touch-icon" href="http://a.xnimg.cn/wap/apple_icon_.png" />
<link rel="stylesheet" type="text/css" href="http://s.xnimg.cn/a86614/nx/core/base.css">
<script type="text/javascript">
if(typeof nx === 'undefined'){
var nx = {};
}
nx.log = {
startTime : + new Date()
};
nx.user = {
id : "972069634",
ruid:"972069634",
tinyPic	: "http://head.xiaonei.com/photos/0/0/men_tiny.gif ",
name : "新用户13211",
privacy: "99",
requestToken : '706736561',
_rtk : 'f5e0f00b'
};nx.user.isvip = false;nx.user.hidead = false;nx.webpager = nx.webpager || {};
nx.production = true;
</script>
"""
def parse_text():
    htmlElement=etree.HTML(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))
def parse_file():
    # #使用Xml解析
    # htmlElement=etree.parse("renren.html")
    # print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
    #使用Html解析
    parse=etree.HTMLParser(encoding="utf-8")
    htmlElement=etree.parse("renren.html",parser=parse)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
if __name__ == '__main__':
    # parse_text()
    parse_file()

























