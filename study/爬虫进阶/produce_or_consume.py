# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/30 22:13
"""
import threading
import random
import time

G_money = 1000
Tatal_times = 20
times = 0

lock = threading.Lock()


class produce(threading.Thread):
    def run(self):
        global G_money, times
        while True:
            if times >= Tatal_times:
                break
            lock.acquire()
            money = random.randint(100, 1000)
            G_money += money
            times += 1
            lock.release()
            print("{}生产了{}元，剩余{}元".format(threading.current_thread(), money, G_money))
            time.sleep(0.5)


class consume(threading.Thread):
    def run(self):
        global G_money, times
        while True:
            money = random.randint(100, 1000)
            lock.acquire()
            if G_money >= money:
                G_money -= money
                print("{}消费了{}元，剩余{}元".format(threading.current_thread(), money, G_money))
            else:
                if times>=Tatal_times:
                    lock.release()
                    break
                print("{}准备消费{}元，剩余{}元，余额不足".format(threading.current_thread(), money, G_money))
            lock.release()
            time.sleep(0.5)



if __name__ == '__main__':
    for i in range(1, 5):
        t = consume(name="消费者线程{}".format(i))
        t.start()
    for i in range(1, 10):
        produce(name="生产者线程{}".format(i)).start()
