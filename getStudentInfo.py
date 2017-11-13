#! ~/bin/python3
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import os
import codecs


class StudentPage(object):
    def __init__(self, id1, id2):
        self.URL = {
            'jbxx': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jbxx_gr.jsp?yonghm=201731",
            'grade': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_score_gr.jsp?yonghm=201731",
            'zizhu': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_zizhu_gr.jsp?yonghm=201731",
            'jtcy': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtcy_gr.jsp?yonghm=201731",
            'jtjj': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtjj_gr.jsp?yonghm=201731",
            'pingbi': "room.bipt.edu.cn/room/xxtj_pingbi_room_ck_pic_R.jsp?xsyhm=201731",
            'pingyu': "xsfw.bipt.edu.cn/fwzx/xspt/xxtj/xxtj_xs_pingyu_0.jsp?yonghm=201731",
            'job': "xsfw.bipt.edu.cn/fwzx/xspt/job/xxcx_job_xsgw_jl.jsp?xsyhm=201731",
            'photo': "xsfw.bipt.edu.cn/fwzx/xs_photo/201731"
        }
        self.Content = {}

        if len(str(id1)) == 1:
            self.id1 = "0" + str(id1)
        else:
            self.id1 = str(id1)

        if len(str(id2)) == 1:
            self.id2 = "000" + str(id2)
        elif len(str(id2)) == 2:
            self.id2 = "00" + str(id2)
        elif len(str(id2)) == 3:
            self.id2 = "0" + str(id2)
        else:
            self.id2 = str(id2)

        self.id = self.id1 + self.id2

        for (k, v) in self.URL.items():
            self.URL[k] += self.id
        self.URL['photo'] += '.jpg'

        for (k, v) in self.URL.items():
            if k != 'photo':
                Content = requests.get('http://' + v).text
                self.Content[k] = Content
            else:
                cnt = requests.get('http://' + v).content
                self.Content[k] = cnt


for id in range(1, 1657):
    student = StudentPage(id1="", id2=id)
    path = '/home/sun/workspace/data/bipt_student_info/17/' + student.id
    # print(path)
    # input()
    os.mkdir(path)
    for (k, v) in student.Content.items():
        if k != 'photo':
            filename = k + '.html'
            try:
                codecs.open(path + '/' + filename, 'w', 'gbk').write(v)
            except:
                pass
        else:
            filename = k + '.jpg'
            try:
                open(path + '/' + filename, 'wb').write(v)
            except:
                pass
    print(student.id, '爬取完毕')
