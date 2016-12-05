# 文件操作类
import  os
class FileRobot():
	def __init__(self):
		pass

	#文件夹的名字不能含有的特殊符号，windows下的限定
	def get_format_filename(self,input_filename):  #
		for s in ['?', '*', '<', '>', '\★', '！', '/','!']:
			while s in input_filename:
				input_filename = input_filename.strip().replace(s, '')
		return input_filename

	#给定目录下创建文件夹
	def creat_folder(self,input_location,input_foldername):
		input_foldername=self.get_format_filename(input_foldername)
		if not os.path.exists(input_location+'\\'+input_foldername):
			try:
				os.makedirs(input_location+'\\'+input_foldername)
				return input_location+'\\'+input_foldername
			except:
				return False
		else:
			return input_location+'\\'+input_foldername
	#打开txt文件，写入文件;style_flag写入方式，1覆盖写入，2继续写入，3换行继续写入
	def write_text(self,input_file_location,input_file_name,input_text,style_flag=1):
		input_file_name=self.get_format_filename(input_file_name)
		try:
			os.chdir(input_file_location)  # 切换到上面创建的文件夹
			if style_flag==1:
				f = open(input_file_name + '.txt', 'w')  # r只读，w可写，a追加
				f.write(input_text)
				f.close()
			elif style_flag==2:
				f = open(input_file_name + '.txt', 'a')  # r只读，w可写，a追加
				f.write(input_text)
				f.close()
			elif style_flag==3:
				f = open(input_file_name + '.txt', 'a')  # r只读，w可写，a追加
				f.write('\n'+input_text)
				f.close()
			return True
		except:
			return False