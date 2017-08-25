import re
s = '13北京市市辖区朝阳区安定路１２号院国典华园７号楼４单元１１０３(asdf)'
print(re.compile(
    '''[^\x00-\xff ·:\[\]*#/\(.*\)^\x00-\xff a-zA-Z0-9-\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+''').findall(s))
print(re.compile("\(.*\)").findall(s))
