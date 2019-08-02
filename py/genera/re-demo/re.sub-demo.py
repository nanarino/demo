'''
输入height165weight21deep213

要求返回height170weight26deep218

也就是数字内容都加5
'''
import re

print(
    re.sub(r'(?P<num>[0-9]+)', lambda x: str(int(x.group("num")) + 5),
           'height165weight21deep213'))
