# input_text_cn,input_text_en为中英文文本信息；input_view_level为当前view等级，input_href为页面url
class Item():
	def __init__(self,input_text_cn='cn',input_text_en='en',input_view_level=2,input_href='href',input_filepath=''):
		self.text_cn=input_text_cn
		self.text_en = input_text_en
		self.href=input_href
		self.view_level = input_view_level
		self.filepath = input_filepath
	def set_text_cn(self,input_text_cn='cn'):
		self.text_cn = input_text_cn
	def set_text_en(self,input_text_en='en'):
		self.text_en=input_text_en
	def set_href(self,input_href):
		self.href=input_href
	def set_filepath(self, input_filepath):
		self.filepath = input_filepath