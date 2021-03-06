#导入需要的模块
import os
import re
import time
import random

import gui
import functions
import cartoonmad
from setting import Setting


#目前爬一张图片的时间在2~4秒左右，可以使用异步之类的操作来提高下载速度，可是下载频率高了后可能会被该网站视为爬虫,要改进的话只能使用多个ip。
#获取某本漫画的界面源代码，并进行转码，由于网站使用big5编码，所以此处也这么用，否则会乱码
info = gui.Get_info()
input_url = info.url
input_folder_path = info.folder_path





download_info = Setting()
url_return = functions.get_html_resource(input_url,download_info.headers)
url_return.encoding = cartoonmad.html_encoding()

info_dict = cartoonmad.extract_comic_info(url_return)
image_url_prefixion = cartoonmad.get_image_url_prefixion(input_url)              
total_info_dict = cartoonmad.form_image_url(info_dict,input_folder_path,image_url_prefixion) 
tm = gui.Choose_chapter(total_info_dict.keys())
choosed_chapter_list = tm.choosed_chapter_list    

print(choosed_chapter_list)

for chapter_info,page_url in total_info_dict.items():
    if not chapter_info in choosed_chapter_list:
        continue
    folder_path = input_folder_path+'/'+chapter_info     
    folder_status = os.path.exists(folder_path)
    if not folder_status :
        os.makedirs(folder_path)                                                #创建每一话文件夹的路径，已存在的话跳过
    pages = len(page_url.keys())                                                #用于提示进度
    print('目前正在下载  '+chapter_info+'----------------------------------')     
    image_list = os.listdir(folder_path+'/')
    image_total_num = len(image_list)                                           #确定该文件下已有多少张图片
    print('进度-------------------------'+'  '+str(image_total_num)+' / '+str(pages)) 
    for page,image_url in page_url.items():
        try:
            image_path = folder_path+'/'+chapter_info+'-'+str(page)+'.jpg'      
            image_status = os.path.exists(image_path)
            if not image_status:                                                     #检测图片是否已下载，未下载的话会进行下载，否则会跳过
                image = functions.get_html_resource(image_url,download_info.headers)
                functions.save_image(image_path,image)
            else:
                print(chapter_info+'-'+str(page)+'.jpg'+'  已下载')
                continue
        except:
            print('\n异常发生，暂停10秒后继续>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('此异常会导致有一张图片的下载被跳过，重新运行此程序后便可补上这张图片>>>>>>>>>>>>>>>>>>>>>\n')
            time.sleep(10)
            continue
        else:
            print(chapter_info+'-'+str(page)+'.jpg'+'  下载完成')
            time.sleep(random.uniform(0.7,2))
    print(chapter_info+' 已完成下载')
            
        























