#! ~/bin/python3
# coding: utf-8
from bs4 import element
from bs4 import BeautifulSoup
import requests
import os
import codecs
import re


class Student(object):
    def __init__(self):
        self.jbxx = ['当前状态', '校园卡号', '姓名', '性别', '年级', '所属院系', '专业', '政治面貌', '班级', '生源地', '民族', '出生日期',
                     '手机号', '邮政编码',  '户口所在地', '考生类别', '科类', '投档成绩', '家庭地址',  '考生特长', '奖惩情况',
                     '考生特征',  '毕业中学']
        self.grade = ['序号',	'学期',	'课程编号',	'课程名称',
                      '学分',	'课程性质'	, '成绩',	'考试类型']
        self.job = ['序号',	'部门',	'岗位名称',
                    '类别',	'酬金标准',	'起始时间',	'终止时间']
        self.jtcy = ['关系',	'姓名',	'出生日期',
                     '现工作单位及职务',	'固定电话',	'手机号码',	'月收入']
        self.jtjj = ['是否烈士子女'	,	'是否孤儿',
                     '是否单亲家庭'	,	'单亲类型',
                     '是否重度残疾'	,	'家庭人均月收入(元)'	,
                     '是否有低收入证明'	,	'是否有低保证明',
                     '是否家庭受灾'	,	'是否家庭遭遇突发意外事件'	,
                     '是否有家庭主要成员残疾'	,	'是否有优抚对象子女证明'	,
                     '是否有北京市城市居民困难补助金领取证'	,	'是否绿色通道'	,
                     '是否务农'	,	'家庭成员健康状况'	 '家庭成员均健康'
                     '家庭经济情况'	]
        self.pingbi = ['班级',	'姓名',	'学年学期'	,
                       '公寓楼'	, '宿舍'	, '周次'	, '宿舍成绩']
        self.zizhu = ['序号',	'类别',	'时间',	'金额']
        self.attr = self.jbxx + self.grade + self.job + \
            self.jtcy + self.jtjj + self.pingbi + self.zizhu


def getDirList(path):
    dirs = os.listdir(path)
    # b = [x for x in a if os.path.isfile(p + x)]
    return dirs


def getSoup(path, pageName):
    filename = path + '/' + pageName
    soup = BeautifulSoup(open(filename, encoding='gbk'), 'lxml')
    return soup


def getJbxx(path):
    soup = getSoup(path, 'jbxx.html')
    info = []
    info_clean = []
    try:
        for tag in soup.table.find_all('td'):
            info.append(str(tag.contents[0]))
        hanzi = [1, 7,  9, 13, 15, 17, 21, 23,  37, 39, 41, 51, 55, 59, 61, 63]
        shuzi = [5, 11, 27, 33, 35, 43]
        other = [19]
        exp = ['''[\u4e00-\u9fa5 ·:\[\]*#/\(\);_－,.!?\^@\$\|`～~○０-９　　　！、—-｀——〇＃￥%&……【】Ⅵ．：，。ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺa-zA-Z0-9-\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+''',
               "[0-9-]+", "[\u4e00-\u9fa5]+[0-9-]+"]
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
                    except Exception as e:
                        info_clean.append('NULL')
            elif num in shuzi:
                try:
                    info_clean.append(re.compile(exp[1]).findall(info[num])[0])
                except Exception as e:
                    info_clean.append('NULL')
            elif num in other:
                try:
                    info_clean.append(re.compile(exp[2]).findall(info[num])[0])
                except Exception as e:
                    info_clean.append('NULL')
    except Exception as e:
        print(path)
        print(str(e))
        # input()
    return info_clean


def getGrade(path):
    soup = getSoup(path, 'grade.html')
    tbody = soup.table.tbody
    info = []
    for div in tbody.find_all('div'):
        info.append(div.contents[0].strip())
    return info


def getJob(path):
    soup = getSoup(path, 'job.html')
    tbody = soup.table.tbody
    info = []
    if len(tbody.contents) != 1:
        for div in tbody.find_all('div'):
            info.append(div.contents[0].strip())
    # 注意勤工助学可能为空
    return info


def getJtcy(path):
    soup = getSoup(path, 'jtcy.html')
    info = []
    try:
        for tr in soup.table.find_all('tr'):
            for td in tr.find_all('td'):
                info.append(td.contents[0])
        # 注意家庭成员可能为空
        # print(info[7:-1])
    except Exception as e:
        pass
    return info[7:-1]


def getJtjj(path):
    soup = getSoup(path, 'jtjj.html')
    info = []
    try:
        for tr in soup.table.find_all('tr'):
            for td in tr.find_all('td'):
                # print(type(td.contents[0]))
                if type(td.contents[0]) is element.NavigableString:
                    info.append(td.contents[0].strip())
        # 判断家庭经济是否每一项都是NULL
        isNull = True
        for e in info:
            if len(e) != 0:
                isNull = False
    except Exception as e:
        # print(path)
        # print(str(e))
        isNull = True
        # input()
    if isNull:
        return []
    else:
        return info


def getPingbi(path):
    soup = getSoup(path, 'pingbi.html')
    info = []
    for tr in soup.table.find_all('tr'):
        for td in tr.find_all('td'):
            if type(td.contents[0]) is element.NavigableString and len(td.contents) == 1:
                info.append(td.contents[0].strip())
            elif len(td.contents) == 3:
                try:
                    info.append(td.contents[1].contents[0] + td.contents[2])
                except Exception as e:
                    info.append('100')
    return info


def getPingyou(path):
    soup = getSoup(path, 'pingyu.html')
    info = []
    try:
        words = soup.find('input')['value']
        info.append(words)
    except Exception as e:
        info.append('')
    return info


def getZizhu(path):
    soup = getSoup(path, 'zizhu.html')
    info = []
    for tr in soup.table.find_all('tr'):
        for td in tr.find_all('td'):
            info.append(td.contents[0])
    info = info[4:-1]
    return info


student = Student()
f = open('info2.csv', 'a')
tmp = ""
for e in student.jbxx:
    tmp += (str(e) + '~')
print(tmp)
f.write(tmp[:-1])
f.write('\n')
for i in range(4, 18):
    path = "/home/sun/workspace/data/bipt_student_info/" + str(i)
    dirs = getDirList(path)
    for dir in dirs:
        path_dir = path + '/' + dir
        print(path_dir)
        line = []
        line.append(getJbxx(path_dir))
        # line.append(getGrade(path_dir))
        # line.append(getJob(path_dir))
        # line.append(getJtcy(path_dir))
        # line.append(getJtjj(path_dir))
        # line.append(getPingbi(path_dir))
        # line.append(getPingyou(path_dir))
        # line.append(getZizhu(path_dir))
        print(path_dir)
        tmp = ""
        for e in line[0]:
            tmp += (e + '~')
        f.write(tmp[:-1])
        f.write('\n')
        # print(path_dir)
        #     input()
        # input()
# break
f.close()
