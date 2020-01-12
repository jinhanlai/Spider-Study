# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/9/1 16:31
"""
import requests
import re
import csv

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.'
                  '36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer': "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&"
               "cl=false&fromSearch=true&labelWords=&suginput=",
    'Host': "www.lagou.com",
    'X-Anit-Forge-Code': "0",
    'X-Anit-Forge-Token': "None",
    'X-Requested-With': "XMLHttpRequest",
    'Origin': "https://www.lagou.com",

    'Accept': "application/json, text/javascript, */*; q=0.01"
}


def parfe_content(url, writer):
    response = requests.get(url=url, headers=header)
    text = response.text
    # print(text)
    positionname = re.findall('<h2\sclass="name">(.*?)</h2>', text, re.DOTALL)
    money = re.findall('<span\sclass="salary">(.*?)</span>', text, re.DOTALL)
    requires = re.findall(r'<dd\sclass="job_request">.*?<h3>.*?</span>(.*?)</h3>', text, re.DOTALL)[0]

    print(url, requires)

    x = re.sub(r'<span>|</span>|/', "", requires.strip()).strip()
    xx = re.split(r'\n', x)
    city = xx[0].strip()
    jinyan = xx[1].strip()
    xueli = xx[2].strip()
    fangshi = xx[3].strip()
    fsd = re.findall('<div\sclass="job-detail">(.*?)</div>', text, re.DOTALL)[0]

    detail = re.sub('<.*?>', "", fsd).strip()
    print(detail)
    # writer.writerow((positionname,money,city,jinyan,xueli,fangshi,detail))


def spilder():
    fp = open('lagou.csv', 'a', encoding='utf-8', newline="")
    writer = csv.writer(fp)
    writer.writerow(('岗位名称', '工资', "城市", "经验", "学历", "工作方式", "具体描述"))
    head_url = "https://www.lagou.com/jobs/"
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    urls = "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
    s = requests.Session()
    # 获取搜索页的cookies
    s.get(urls, headers=header, timeout=1)
    # 为此次获取的cookies
    cookie = s.cookies
    # 获取此次文本
    for x in range(1, 10):
        data['pn'] = x
        response = s.post(url, data=data, headers=header, cookies=cookie, timeout=1)
        result = response.json()
        positons = result["content"]["positionResult"]["result"]
        for posi in positons:
            posit_id = posi["positionId"]
            parfe_content(head_url + str(posit_id) + ".html", writer)


if __name__ == '__main__':
    spilder()
