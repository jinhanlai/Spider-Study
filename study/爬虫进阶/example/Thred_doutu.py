# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/31 15:22
"""
import os
import requests
from threading import Thread
import re
from queue import Queue


class produce(Thread):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }

    def __init__(self, pageQueue, img_Queue, *args, **kwargs):
        super(produce, self).__init__(*args, **kwargs)
        self.pageQueue = pageQueue
        self.img_Queue = img_Queue

    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            url = self.pageQueue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url=url, headers=self.header)
        text = response.text
        # print(text)
        img_url = re.findall('<img\sreferrerpolicy="no-referrer".*?data-original="(.*?)".*?>', text, re.DOTALL)
        alt = re.findall('<img\sreferrerpolicy="no-referrer".*?alt="(.*?)".*?>', text, re.DOTALL)
        houzui = list(map(lambda x: os.path.splitext(x)[1], img_url))  # 获取文件后缀名

        for i in range(0,len(img_url)):
            filename=alt[i] + houzui[i]
            # print((img_url[i],filename))
            self.img_Queue.put((img_url[i],filename))


class consum(Thread):
    def __init__(self, page_Queue, img_Queue, *args, **kwargs):
        super(consum, self).__init__(*args, **kwargs)
        self.page_Queue = page_Queue
        self.img_Queue = img_Queue

    def run(self):
        while True:
            if self.img_Queue.empty() and self.page_Queue.empty():
                break
            img_url,filename=self.img_Queue.get()
            res = requests.get(img_url)
            with open('images/' + filename, 'wb') as f:
                f.write(res.content)

if __name__ == '__main__':
    page_Queue = Queue(100)  # 用来放每个page的url
    img_Queue = Queue(1000)  # 用来放爬取的每个图片的链接

    for i in range(1, 101):
        url = "http://www.doutula.com/photo/list/?page={}"
        page_Queue.put(url.format(i))
    for x in range(5):
        t = produce(page_Queue, img_Queue)
        t.start()
    for x in range(5):
        t = consum(page_Queue, img_Queue)
        t.start()
