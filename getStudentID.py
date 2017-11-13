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


# 判断某一届学生学号结束的数字
for id1 in range(17, 18):
    print('正在获取 0', id1, '级最后一位学号，需要一点时间....')
    for id in range(2000, -1, -1):
        student = StudentPage(id1="", id2=id)
        print(student.URL['jbxx'])
        r = requests.get("http://" + student.URL['jbxx'])
        soup = BeautifulSoup(r.text, "lxml")
        if soup.find_all('th') != []:
            print(id1, '级 ', student.id, ' 是最后一个学号')
            break
        else:
            pass

    # break
