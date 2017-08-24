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


def getDirList(path):
    dirs = os.listdir(path)
    # b = [x for x in a if os.path.isfile(p + x)]
    return dirs


def getJbxx(path):
    filename = path + '/' + 'jbxx.html'
    # pagetext = ''
    # f = open(filename, mode='r', encoding='gbk')
    # pagetext = f.read()
    # f.close()
    # soup = BeautifulSoup(pagetext, 'lxml')
    # text = soup.get_text()
    # print(text)
    soup = BeautifulSoup(open(filename, encoding='gbk'), 'lxml')
    th = soup.table.th
    print(type(th))
    # for tag in th.find_all(re.compile("[\u4e00-\u9fa5]+")):
    for tag in th.find_all(re.compile("[a-z]+")):
        print(tag.name)


# path = "/home/sun/workspace/temp"
path = "/home/sun/workspace/data/bipt_student_info/16"
dirs = getDirList(path)
for dir in dirs:
    getJbxx(path + '/' + dir)
    break
