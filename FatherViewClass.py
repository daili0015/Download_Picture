# 处理父页面，父页面是包含各种项目的页面
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ItemClass import Item
from bs4 import BeautifulSoup
import time
class FatherView():
	def __init__(self,input_url='http://www.plantphoto.cn/class?m=2',input_category='某某植物',input_browser=1):
		self.url=input_url#默认值为苔藓植物页面
		self.category=input_category
		self.browser=input_browser
	#set函数
	def set_url(self,input_url):
		self.text=input_url
	def set_category(self,input_category):
		self.category=input_category
	def set_browser(self,input_browser):
		self.browser=input_browser
	# 获取一个driver,1PhantomJS() 2PhantomJS()
	def get_driver(self):
		if self.browser==1:
			return  webdriver.PhantomJS()
		else:
			return  webdriver.Chrome()
	def Process_View(self):
		driver =self.get_driver()
		driver.get(self.url)
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滚到最底部，提示服务器加载更多
		try:
			WebDriverWait(driver, 30).until(  # 加载完毕的标志
				EC.presence_of_element_located((By.CLASS_NAME, "mp10"))
			)
		except:
			print('加载失败，没找到指定元素')
		finally:
			print('确认加载完毕，开始向下翻页')
			element_num_list = list()  # 存储页面当前有多少项目（科）
			for i in range(300):  # 循环多次，每次向下翻到最后，然后选取其中的项目
				print()
				driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
				time.sleep(2)
				element_num_list.append(len(driver.find_elements_by_class_name("mp10")))
				print('第' + str(i) + '次翻页操作，当前项目有' + str(element_num_list[i]) + '个')
				if i >= 3 and element_num_list[i] == element_num_list[i - 1] and element_num_list[i] == \
						element_num_list[i - 2]:
					break#连续三个翻页翻不出新东西来，认为到底了
		bsObj = BeautifulSoup(driver.page_source, 'html.parser')
		son_item_list = list()  # 装子项目的list
		for single_item in bsObj.find("div", {"class": "item_list infinite_scroll masonry"}) \
				.findAll("div", {"class": "item3 masonry_brick imgdivh masonry-brick"}):
			son_item = Item()
			son_item.set_text(single_item.find("div", {"style": "text-align:left;"}).find("a").text)
			son_item.set_href('http://www.plantphoto.cn/'+single_item.find("div", {"style": "text-align:left;"}).find("a").attrs['href'])
			son_item_list.append(son_item)
		return son_item_list#返回包含子item的列表
