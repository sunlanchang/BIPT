## 北京石油化工学院成绩爬虫   
`python -verson python3  `
- `MajorRank.py`为查看学院学生排名
- `SomeoneGrade.py`为查询单个学生成绩  
```
各年级最后一个学号
4 级  041718  
5 级  051662  
6 级  061608  
7 级  071603  
8 级  081687  
9 级  091690  
10 级  101683 
11 级  111693 
12 级  121696  
13 级  131683  
14 级  141656  
15 级  151612  
16 级  161652  
```
## 提取数据
`jbxx.py`用来提取学生基本信息页面的数据。  
- 使用BeautifulSoup和正则表达式进行提取。  
其余页面用bs4的find_all()提取表格数据。  
- `find_all()`提取  