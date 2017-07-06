#! ~/bin/python3
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import os
import codecs


class StudentPage(object):
    def __init__(self, id1, id2):
        self.URL = {
            'jbxx': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jbxx_gr.jsp?yonghm=5120",
            'grade': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_score_gr.jsp?yonghm=5120",
            'zizhu': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_zizhu_gr.jsp?yonghm=5120",
            'jtcy': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtcy_gr.jsp?yonghm=5120",
            'jtjj': "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtjj_gr.jsp?yonghm=5120",
            'pingbi': "room.bipt.edu.cn/room/xxtj_pingbi_room_ck_pic_R.jsp?xsyhm=5120",
            'pingyu': "xsfw.bipt.edu.cn/fwzx/xspt/xxtj/xxtj_xs_pingyu_0.jsp?yonghm=5120",
            'job': "xsfw.bipt.edu.cn/fwzx/xspt/job/xxcx_job_xsgw_jl.jsp?xsyhm=5120",
            'photo': "xsfw.bipt.edu.cn/fwzx/xs_photo/5120"
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


# 判断某一届学生学号结束的数字
for class_ in range(4, 17):
    for id in range(2000, -1, -1):
        student = StudentPage(class_, id)
        r = requests.get("http://" + student.URL['jbxx'])
        soup = BeautifulSoup(r.text, "lxml")
        if soup.find_all('th') != []:
            print(class_, '级 ', student.id, ' 是最后一个学号')
            break
        else:
            pass

    # break
