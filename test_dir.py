#! ~/bin/python3
# coding: utf-8

import os
from bs4 import BeautifulSoup
import requests

jbxx = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jbxx_gr.jsp?yonghm=5120150752"
grade = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_score_gr.jsp?yonghm=5120150752"
photo = "xsfw.bipt.edu.cn/fwzx/xs_photo/5120150752.jpg"
id = "150752"
jbxx_text = requests.get('http://' + jbxx).text
grade_text = requests.get('http://' + grade)
path = '/home/sun/workspace/data/' + id
os.mkdir(path)
# with open(path + '/' + 'jbxx.html', 'w') as f:
#     f.write(jbxx_text)
r = requests.get('http://' + photo)
if r.status_code == 200:
    print('test')
    open(path + '/' + 'photo.jpg', 'wb').write(r.content)
