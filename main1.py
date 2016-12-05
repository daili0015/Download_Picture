
from FatherViewsubClass import FatherViewsub
from FatherViewClass import FatherView
URL='http://www.plantphoto.cn/fam/1099'

f_s=FatherView(input_url=URL,input_category_cn='白花菜属',input_View_level=2,\
               input_browser=2,input_floderpath='D:\MyProjectFile\Python\studyproject\Python3\selenium_study\database\白花菜属')
sdo=f_s.Process_View()

son=sdo[1]
son_url=son.href
son_cn=son.text_cn
son_en=son.text_en
son_path=son.filepath

ff_s=FatherViewsub(son_url,input_category_cn=son_cn,input_category_en=son_en,input_browser=2,input_floderpath=son_path)
ff_s.Process_View()

print('hello')

