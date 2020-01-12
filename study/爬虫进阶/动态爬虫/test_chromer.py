#_*_ coding:utf-8 _*_
"""
 @author: LaiJinHan
 @time：2019/9/1 10:30
"""
from selenium import webdriver

driver_path=r"D:\ProgrameApp\chromedriver\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
print(driver.page_source)

driver.close()#关闭当前页面
driver.quit()#退出浏览器