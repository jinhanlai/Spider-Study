# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/30 23:22
"""
from queue import Queue
import time
import threading


def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)


def get_value(q):
    while True:
        print(q.get())  # get,和put都是阻塞模式，get时当queue为空时，会一直等待直到有数据
        # q.get(block=True)


if __name__ == '__main__':
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])

    t1.start()
    t2.start()
