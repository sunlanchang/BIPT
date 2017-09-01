#! ~/bin/python3
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import os
import codecs
import re


class Student(object):
    def __init__(self):
        self.jbxx = {'校园卡号': '', '姓名': '', '性别': '', '年级': '', '所属院系': '', '专业': '', '班级': '', '民族': '', '出生日期': '',
                     '住宿地址': '', '邮政编码': '', '考生类别': '', '投档成绩': '',  '数学成绩': '', '家庭地址': '', '考生特长': '', '奖惩情况': '',
                     '考生特征': '', '政审意见': '', '毕业中学': '', '备注': '', '政治面貌': '', '生源地': '', '班级职务': '', '外语语种': '', '手机号': '', '户口所在地': '',
                     '科类': '', '语文成绩': '', '外语成绩': '', '班主任': ''}
        self.grade = {'序号': '',	'学期': '',	'课程编号': '',	'课程名称': '',
                      '学分': '',	'课程性质'	: '', '成绩': '',	'考试类型': ''}


def getDirList(path):
    dirs = os.listdir(path)
    # b = [x for x in a if os.path.isfile(p + x)]
    return dirs


def getJbxx(path):
    filename = path + '/' + 'jbxx.html'
    soup = BeautifulSoup(open(filename, encoding='gbk'), 'lxml')
    info = []
    for tag in soup.table.find_all('td'):
        info.append(str(tag.contents[0]))
    hanzi = [1, 7,  9, 13, 15, 17, 21, 23,  37, 39, 41, 51, 55, 59, 61, 63]
    shuzi = [5, 11, 27, 33, 35, 43]
    other = [19]
    exp = ['''[\u4e00-\u9fa5 ·:\[\]*#/\(\);_－,.!?\^@\$\|`～~○０-９　　　！、—-｀——〇＃￥%&……【】Ⅵ．：，。ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺa-zA-Z0-9-\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+''',
           "[0-9-]+", "[\u4e00-\u9fa5]+[0-9-]+"]
    info_clean = []
    for num in range(len(info)):
        if num in hanzi:
            tmp = re.compile(exp[0]).findall(info[num])
            # info_clean.append(tmp)
            if len(tmp) > 1:
                tmps = ''
                for e in tmp:
                    tmps += e
                info_clean.append(tmps)
            else:
                try:
                    info_clean.append(tmp[0])
                except:
                    print('tmp', tmp)
                    input()
                    info_clean.append('NULL')
        elif num in shuzi:
            try:
                info_clean.append(re.compile(exp[1]).findall(info[num])[0])
            except:
                info_clean.append('NULL')
        elif num in other:
            try:
                info_clean.append(re.compile(exp[2]).findall(info[num])[0])
            except:
                info_clean.append('NULL')
    print(info_clean)
    print(len(info_clean))


def getGrade(path):
    filename = path + '/' + 'grade.html'
    soup = BeautifulSoup(open(filename, encoding='gbk'), 'lxml')
    # print(soup)
    tbody = soup.table.tbody
    # print(tbody)
    for div in tbody.find_all('div'):
        print(div.contents[0])


def getJob(path):
    filename = path + '/' + 'job.html'
    soup = BeautifulSoup(open(filename, encoding='gbk'), 'lxml')
    tbody = soup.table.tbody
    # print(tbody.contents)
    if len(tbody.contents) != 1:
        for div in tbody.find_all('div'):
            print(div.contents)
        # input('input: ')
    else:
        pass


path = "/home/sun/workspace/data/bipt_student_info/14"
dirs = getDirList(path)
for dir in dirs:
    # getJbxx(path + '/' + dir)
    # getGrade(path + '/' + dir)
    getJob(path + '/' + dir)
    # input()
    # break
