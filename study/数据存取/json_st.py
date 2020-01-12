# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/8/30 19:19
"""
import json
#
# #存储json格式数据
# persons = [
#     {
#         'username': "张三",
#         'age': 18,
#         'country': 'china'
#     },
#     {
#         'username': '李赛',
#         'age': 20,
#         'country': 'china'
#     }
# ]
#
# json_str = json.dumps(persons)
# with open('person.json', 'w', encoding='utf-8') as fp:
#     # fp.write(json_str)#这个字符串编码不对
#     json.dump(persons, fp, ensure_ascii=False,indent=2)#indent=2是下一行的空格为2个

# json_str = '[{"username": "张三", "age": 18, "country": "china"}, {"username": "李赛", "age": 20, "country": "china"}]'
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)
#
# with open('person.json','r',encoding='utf-8') as fp:
#     persons = json.load(fp)
#     print(type(persons))
#     for person in persons:
#         print(person)
