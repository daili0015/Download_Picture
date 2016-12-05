# 专门处理属页面
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ItemClass import Item
from bs4 import BeautifulSoup
from FileRobotClass import FileRobot
import time

min_element=9#设定每一页最少的element数
class FatherViewsub():
	def __init__(self,input_url='http://www.plantphoto.cn/class?m=2',
	             input_category_cn='cn',input_category_en='en',input_browser=1,input_floderpath=''):
		self.url=input_url#默认值为苔藓植物页面
		self.category_cn = input_category_cn
		self.category_en = input_category_en
		self.browser=input_browser
		self.introduction = ''
		self.floderpath=input_floderpath
		self.son_item_list = list()  # 装子项目的list
	#set函数
	def set_View_level(self,input_View_level):
		self.View_level=input_View_level
	def set_url(self,input_url):
		self.text=input_url
	def set_category(self,input_category_cn,input_category_en):
		self.category_en = input_category_en
		self.category_cn = input_category_cn
	def set_browser(self,input_browser):
		self.browser=input_browser
	def set_floderpath(self,input_floderpath):
		self.floderpath=input_floderpath

	# 获取一个driver,1PhantomJS() 2Chrome()
	def get_driver(self):
		if self.browser==1:
			return  webdriver.PhantomJS()
		else:
			return  webdriver.Chrome()

	# 信息写入文本，建立子文件夹操作函数
	def flie_writer(self):
		Robot1 = FileRobot()
		ind=0
		for son in self.son_item_list: #为子目录建立文件夹
			try:
				file_folder=Robot1.creat_folder(self.floderpath, str(ind+1)+son.text_en)
				self.son_item_list[ind].set_filepath(file_folder)
				son_text='学名：'+son.text_cn+'\n地点信息：'+son.text_en+'\nURL：'+son.href
				Robot1.write_text(file_folder, son.text_cn + '简介', son_text, style_flag=1)
				# 下面的message文件为其索引等信息，提供给开发者
				index_text = son.text_cn + '#' + son.text_en + '#'+ son.href + '#'+ self.url
				Robot1.write_text(file_folder, 'index_message', index_text.strip(), style_flag=1)
			except:
				print('建立子页面文件夹出错！')
			ind+=1
		#为自己写入简介，在父建立的txt文档后写入
		Robot1.write_text(self.floderpath,self.category_cn+'简介','简介：\n'+self.introduction, style_flag=3)

	def Process_View(self):
		driver =self.get_driver()
		driver.get(self.url)
		time.sleep(2)
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滚到最底部，提示服务器加载更多
		try:
			WebDriverWait(driver, 30).until(  # 加载完毕的标志
				EC.presence_of_element_located((By.CLASS_NAME, "item_t"))
			)
		except:
			print('加载失败，没找到指定元素')
		finally:
			print('确认加载完毕，开始向下翻页')
			element_num_list = list()  # 存储页面当前有多少项目（科）
			for i in range(300):  # 循环多次，每次向下翻到最后，然后选取其中的项目
				print()
				driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
				time.sleep(4)
				element_num_list.append(len(driver.find_elements_by_class_name("item_t")))
				print('第' + str(i) + '次翻页操作，当前项目有' + str(element_num_list[i]) + '个')
				if (i >= 3 and element_num_list[i] == element_num_list[i - 1] and element_num_list[i] == \
						element_num_list[i - 2]) or element_num_list[i] < min_element:
					break#连续三个翻页翻不出新东西来，认为到底了
		bsObj = BeautifulSoup(driver.page_source, 'html.parser')
		driver.close()
		self.introduction = bsObj.find("div", {"class": "fl specialdesc"}).text

		for single_item in bsObj.find("div", {"class": "item_list infinite_scroll masonry"}) \
				.findAll("div", {"class": "item3 masonry_brick masonry-brick"}):
			son_item = Item()
			son_item.set_text_cn(single_item.find("div", {"class": "namew fl"}).find("a").text)  # 设置学名
			son_item.set_href('http://www.plantphoto.cn/' + single_item.find("div", {"class": "namew fl"}).find("a").attrs['href'])
			son_item.set_text_en(single_item.find("span").text)  # 设置其他信息 +str(single_item.find("span").next)
			self.son_item_list.append(son_item)
		self.flie_writer()
		return self.son_item_list#返回包含子item的列表
