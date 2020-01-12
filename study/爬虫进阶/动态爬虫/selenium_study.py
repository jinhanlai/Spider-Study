# _*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/9/1 14:43
"""
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = r"D:\ProgrameApp\chromedriver\chromedriver.exe"

# driver = webdriver.Chrome(executable_path=driver_path)


# #如果只是解析网页，可以用正则表达式 或者lxml
# html=etree.HTML(driver.page_source)
# html.xpath("")
#
# driver.get('https://www.baidu.com/')
# #对网页中的元素进行操作,操作输入框
# # inputTag=driver.find_element_by_id('kw')
# # inputTag=driver.find_element(By.CSS_SELECTOR,".quickdelete-wrap > input")
# # print(inputTag)
# inputTag=driver.find_element_by_name('wd')
# # inputTag.send_keys('python')
# submitTag = driver.find_element_by_id('su')
# # submitTag.click()
# # time.sleep(1)
# # inputTag.clear()
##操作链
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'python')
# actions.move_to_element(submitTag)
# actions.click(submitTag)
# actions.perform()


# driver.get('https://www.douban.com/')
# 操作checkbox  url=https://www.douban.com/
# driver.implicitly_wait(20)
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()

# driver.get("http://www.dobai.cn/")
# # 操作select标签  url=http://www.dobai.cn/
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# # selectBtn.select_by_index(1)
# # selectBtn.select_by_value("http://m.95xiu.com/")
# selectBtn.select_by_visible_text("95秀客户端")

# #获得cookie信息
# driver.get("https://www.baidu.com/")
# for cookie in driver.get_cookies():
#     print(cookie)
#
# print('='*30)
#
# print(driver.get_cookie("PSTM"))
#
# driver.delete_cookie("PSTM")
# print('='*30)
# # print(driver.get_cookie('PSTM'))
# driver.delete_all_cookies()

# # 虽然在窗口中切换到了新的页面。但是driver中还没有切换。
# # 如果想要在代码中切换到新的页面，并且做一些爬虫。
# # 那么应该使用driver.switch_to_window来切换到指定的窗口
# # 从driver.window_handlers中取出具体第几个窗口
# # driver.window_handlers是一个列表，里面装的都是窗口句柄。
# # 他会按照打开页面的顺序来存储窗口的句柄。
# driver.get('https://www.baidu.com/')
# driver.execute_script("window.open('https://www.douban.com/')")
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[1])
#
# print(driver.current_url)
# # print(driver.page_source)

# #获得屏幕截图，和当前元素的值
# driver.get('https://www.baidu.com/')
# submitBtn = driver.find_element_by_id('su')
# print(type(submitBtn))
# print(submitBtn.get_attribute("value"))
# driver.save_screenshot('baidu.png')

#使用显示，隐示等待
# driver.get('https://www.douban.com/')
#
# # driver.implicitly_wait(20)
#
# element = WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.ID,'anony-nav'))
# )
# print(element)



# #使用ip代理
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://60.17.239.207:31032")
#
# driver = webdriver.Chrome(executable_path=driver_path,options=options)
#
# driver.get("http://httpbin.org/ip")

