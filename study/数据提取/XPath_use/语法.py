# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/28 9:16
"""
from lxml import etree

# 1.获取所有tr标签
# 2.获取第二个tr标签
# 3.获取所有class等于even的标签
# 4.获取所有a标签的href属性
# 5.获取所有职位信息
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=parser)

#谓词中的下标是从1开始的
# #1.获取所有的tr标签
# #//tr
# #xpath函数返回的是一个列表
# trs=html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

# #2.获取第二个tr标签
# tr=html.xpath("//tr[2]")[0]#因为xpath返回的是一个列表所以加上[0]获取tr标签
# print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

# # 3.获取所有class等于even的标签
# trs=html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

# # 4.获取所有a标签的href属性
# alist=html.xpath("//a/@href")
# for a in alist:
#     print("http://hr.tencent.com/"+a)

# 5.获取所有职位信息
trs=html.xpath("//tr[position()>1]")
positons=[]
for tr in trs:
    a=tr.xpath(".//a/@href")[0]
    href="http://hr.tencent.com/"+a
    titile=tr.xpath("./td[1]//text()")[0]
    category = tr.xpath("./td[2]//text()")[0]
    num = tr.xpath("./td[3]//text()")[0]
    addr = tr.xpath("./td[4]//text()")[0]
    times = tr.xpath("./td[5]//text()")[0]

    posi={
        "url":href,
        "title":titile,
        "category":category,
        "num":num,
        "addr":addr,
        "times":times
    }
    positons.append(posi)
print(positons)















