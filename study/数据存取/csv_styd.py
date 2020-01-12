# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/30 19:27
"""
import csv


def read_csv_demo1():
    with open('classroo1.csv', 'r',encoding='utf-8') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        next(reader)#跳过表头
        for x in reader:
            name = x[0]
            age = x[1]
            print({'name': name, 'age': age})


def read_csv_demo2():
    with open('classroo1.csv', 'r',encoding='utf-8') as fp:
        # 使用DictReader创建的reader对象
        # 不会包含标题那行的数据
        # reader是一个迭代器，遍历这个迭代器，返回来的是一个字典。
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"username": x['username'], 'age': x['age']}
            print(value)


# 相当于excel文件
def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('張三', 18, 180),
        ('李四', 19, 190),
        ('王五', 20, 160)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)  # 写入表头
        writer.writerows(values)  # 写入所有数据


def write_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {'username': '张三', 'age': 18, 'height': 180},
        {'username': '李四', 'age': 19, 'height': 190},
        {'username': '王五', 'age': 20, 'height': 160}
    ]
    with open('classroo1.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        # 写入表头数据的时候，需要调用writeheader方法
        writer.writeheader()  # 写入表头
        writer.writerows(values)


if __name__ == '__main__':
    # write_csv_demo2()
    read_csv_demo2()
