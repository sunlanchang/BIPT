#! ~/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
print('输入学号后六位：')
stuid = input()
url = "http://xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_score_gr.jsp?yonghm=5120" + \
    str(stuid)
response = requests.get(url)
student = []
html = response.content
soup = BeautifulSoup(html, 'lxml')
for element in soup.tbody.find_all('tr'):
    lession = []
    num = 0
    for string in element.stripped_strings:
        if num == 4 or num == 6:
            lession.append(repr(string)[1:len(repr(string)) - 1])
        num += 1
    student.append(lession)


def lession_to_num():
    global student
    for grade in student:
        try:
            float(grade[1])
        except ValueError:
            if '优' == grade[1]:
                grade[1] = '95'
            elif '良' == grade[1]:
                grade[1] = '85'
            elif '中' == grade[1]:
                grade[1] = '75'
            elif '及格' == grade[1]:
                grade[1] = '65'
            elif '通过' == grade[1]:
                grade[1] = '80'
            else:
                grade[1] = 0
                pass


lession_to_num()
sum_credit = 0
GPA = 0
res = []
for grade in student:
    res_2 = []
    for element in grade:
        element = float(element)
        res_2.append(element)
    res.append(res_2)
for grade in res:
    sum_credit += float(grade[0])
    GPA += (float(grade[0]) * float(grade[1]))
    #print(sum_credit, GPA)
try:
    if round(GPA / sum_credit):
        print(sum_credit)
        print(GPA)
        print(round(GPA / sum_credit))
except:
    pass
    print('cuo wu')
