#! ~/bin/python3
# coding: utf-8
import requests
from bs4 import BeautifulSoup


class StudentPage(object):
    URL_jbxx = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jbxx_gr.jsp?yonghm=5120"
    URL_grade = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_score_gr.jsp?yonghm=5120"
    URL_zizhu = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_zizhu_gr.jsp?yonghm=5120"
    URL_jtcy = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtcy_gr.jsp?yonghm=5120"
    URL_jtjj = "xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jtjj_gr.jsp?yonghm=5120"
    URL_pingbi = "room.bipt.edu.cn/room/xxtj_pingbi_room_ck_pic_R.jsp?xsyhm=5120"
    URL_pingyu = "xsfw.bipt.edu.cn/fwzx/xspt/xxtj/xxtj_xs_pingyu_0.jsp?yonghm=5120"
    URL_job = "xsfw.bipt.edu.cn/fwzx/xspt/job/xxcx_job_xsgw_jl.jsp?xsyhm=5120"

    def __init__(self, id1, id2):
        self.id1 = id1
        if len(str(id2)) == 1:
            self.id2 = "00" + str(id2)
        elif len(str(id2)) == 2:
            self.id2 = "0" + str(id2)
        else:
            self.id2 = str(id2)
        self.id = self.id
        self.URL_jbxx = self.URL_jbxx + self.id
        self.URL_grade = self.URL_grade + self.id
        self.URL_zizhu = self.URL_zizhu + self.id
        self.URL_jtcy = self.URL_jtcy + self.id
        self.URL_jtjj = self.URL_jtjj + self.id
        self.URL_pingbi = self.URL_pingbi + self.id
        self.URL_pingyu = self.URL_pingyu + self.id
        self.URL_job = self.URL_job + self.id


# 判断某一届学生学号结束的数字
for id in range(1, 999):
    student = StudentPage("041", 800)
    r = requests.get("http://" + student.URL_jbxx)
    print(r.text)
    if r.text != 200:
        print("结束位置：" + student.id)
        break
    else:
        print(student.id)
