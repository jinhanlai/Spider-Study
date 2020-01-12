#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/30 23:01
"""
import threading
import random
import time

G_money = 1000
Tatal_times = 20
times = 0

condition = threading.Condition()


class produce(threading.Thread):
    def run(self):
        global G_money, times
        while True:
            if times >= Tatal_times:
                break
            condition.acquire()
            money = random.randint(100, 1000)
            G_money += money
            times += 1
            condition.notify_all()#通知wait()的线程继续执行接下来的步骤
            condition.release()
            print("{}生产了{}元，剩余{}元".format(threading.current_thread(), money, G_money))
            time.sleep(0.5)


class consume(threading.Thread):
    def run(self):
        global G_money, times
        while True:
            money = random.randint(100, 1000)
            condition.acquire()
            while G_money<money:  #用while是因为当wait()结束后，还要继续判断G_money是不是充足，因为还有可能小于money
                if times>=Tatal_times:
                    condition.release()
                    return

                print("{}准备消费{}元，剩余{}元，余额不足".format(threading.current_thread(), money, G_money))
                condition.wait()#该线程陷入等待状态

            G_money-=money
            condition.release()
            print("{}消费了{}元，剩余{}元".format(threading.current_thread(), money, G_money))
            time.sleep(0.5)



if __name__ == '__main__':
    for i in range(1, 5):
        t = consume(name="消费者线程{}".format(i))
        t.start()
    for i in range(1, 5):
        produce(name="生产者线程{}".format(i)).start()
