# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/9/1 23:11
"""
from selenium import webdriver
import re
import time
# from PIL import Image

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from scrapy.loader import ItemLoader

class splider(object):
    driver_path = r"D:\ProgrameApp\chromedriver\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.positons = []

    def run(self):
        lagou_url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        self.driver.get(lagou_url)

        while True:
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pager_next'))

            )
            text = self.driver.page_source
            self.parse_page(text)


            # 点击下一页
            next_pag = self.driver.find_element_by_class_name('pager_next')
            is_next = re.findall('pager_next_disabled', text, re.DOTALL)
            if is_next:
                break
            next_pag.click()
            time.sleep(1)
            print("成功加载一页内容")


    def parse_page(self, text):
        """
        :param text: 待爬取得网页
        :return: 爬取到的url链接
        """
        urls = re.findall(r'<div\sclass="p_top">.*?<a\sclass="position_link"\shref="(.*?)".*?>.*?<h3', text, re.DOTALL)
        # print(len(urls))
        for url in urls[0:-1]:
            # print(url)
            self.parse_detail_infor(url)
            time.sleep(1)

    def parse_detail_infor(self, url):
        """
        
        :param url: 待爬取页面的详细信息的url
        :return: 爬取得详细信息
        """
        # 打开另外一个网页进行爬取
        self.driver.execute_script("window.open('" + url + "')")
        # 把driver切换到新打开的页面,self.driver.window_handles存储的是依次打开的窗口
        self.driver.switch_to.window(self.driver.window_handles[1])

        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"name"))
        )

        text = self.driver.page_source
        # print(text)

        positionname = re.findall('<h2\sclass="name">(.*?)</h2>', text, re.DOTALL)
        money = re.findall('<span\sclass="salary">(.*?)</span>', text, re.DOTALL)
        requires = re.findall(r'<dd\sclass="job_request">.*?<h3>.*?</span>(.*?)</h3>', text, re.DOTALL)[0]

        # print(url, requires)
        company = re.findall(r'<h3\sclass="fl">.*?<em\sclass="fl-cn">(.*?)</em>', text, re.DOTALL)[0].strip()
        x = re.sub(r'<span>|</span>|/', "", requires.strip()).strip()
        xx = re.split(r'\n', x)
        city = xx[0].strip()
        jinyan = xx[1].strip()
        xueli = xx[2].strip()
        fangshi = xx[3].strip()
        fsd = re.findall('<div\sclass="job-detail">(.*?)</div>', text, re.DOTALL)[0]
        detail = re.sub('<.*?>', "", fsd).strip()
        position = {
            'title': positionname,
            'city': city,
            'salary': money,
            'company': company,
            'education': xueli,
            'experience': jinyan,
            'type': fangshi,
            'detail': detail
        }
        # print(position)
        self.positons.append(position)
        # 关闭当前页面
        self.driver.close()
        # 回到主页面)、
        self.driver.switch_to.window(self.driver.window_handles[0])
        # print(position)
        # print('=' * 30)


if __name__ == '__main__':
    t = splider()
    t.run()
