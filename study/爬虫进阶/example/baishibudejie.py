# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/31 22:33
"""
import threading
import csv
from queue import Queue
import requests
import csv
import re


class produce(threading.Thread):
    def __init__(self, page_Queue, content_Queue, *args, **kwargs):
        super(produce, self).__init__(*args, **kwargs)
        self.page_Queue = page_Queue
        self.content_Queue = content_Queue

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Appl"
                      "eWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    link_head = "http://www.budejie.com"

    def run(self):
        while True:
            if self.page_Queue.empty():
                break
            url = self.page_Queue.get()
            response = requests.get(url=url, headers=self.header)
            text = response.text
            # print(text)
            contents = re.findall('<div\sclass="j-r-list-c-desc">.*?<a.*?>(.*?)</a>', text, re.DOTALL)

            links = re.findall('<div\sclass="j-r-list-c-desc">.*?<a\shref="(.*?)">', text, re.DOTALL)
            for x in range(0, len(links)):
                link = self.link_head + links[x]
                cont = re.sub(r'<.*?>', ' ', contents[x])

                self.content_Queue.put((cont, link))
            print("加载完页面")


class consum(threading.Thread):
    def __init__(self, content_Queue, gLock, write, *args, **kwargs):
        super(consum, self).__init__(*args, **kwargs)
        self.content_Queue = content_Queue
        self.gLock = gLock
        self.write = write

    def run(self):
        while True:
            # print(self.content_Queue.empty())
            # print(self.content_Queue.get())
            # if self.content_Queue.empty():
            #     break
            conten, link = self.content_Queue.get()
            # print(conten, link)
            self.gLock.acquire()
            self.write.writerow((conten, link))
            self.gLock.release()
            print("保存了一条数据")


if __name__ == '__main__':
    page_Queue = Queue(10)
    content_Queue = Queue(500)
    ur = "http://www.budejie.com/text/{}"
    for i in range(1, 10):
        url = ur.format(i)
        page_Queue.put(url)
    bsbdj = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
    write = csv.writer(bsbdj)
    write.writerow(('content', 'link'))
    gLock = threading.Lock()

    for i in range(5):
        t = produce(page_Queue, content_Queue)
        t.start()

    for i in range(5):
        t = consum(content_Queue, gLock, write)
        t.start()

