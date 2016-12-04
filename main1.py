from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ItemClass import Item
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from FatherViewClass import FatherView

URL='http://www.plantphoto.cn/class?p=D&m=5'

f_s=FatherView(input_url=URL,input_category='报春花属')
sdo=f_s.Process_View()
# driver = webdriver.Chrome()
# driver.get(sdo[0].href)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 滚到最底部，提示服务器加载更多
print('hello')


# elem = driver.find_element_by_name("wd")
# elem.send_keys("nihao")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source) #获取网页渲染后的源代码

# 访问网页，获取title
# driver = webdriver.PhantomJS()
# driver.get("http://hotel.qunar.com/")
# data = driver.title
# print(data)

# 按照规则获取信息
# driver = webdriver.PhantomJS()
# driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
# data = driver.find_element_by_id("jd_comments").text
# print(data)
# driver.quit()