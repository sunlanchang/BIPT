import re
s = '<th colspan="4" height="25">【胡愈志】个人基本信息</th>'
print(re.compile("[\u4e00-\u9fa5]{2,4}").findall(s))
