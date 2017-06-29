# -*- coding: utf-8 -*-
# @Author: linguowei

import re

line = "weiwei123"
regex_str = "^w.*" # 匹配以'w'开头的任意字符串，'^w'代表w开头, '.'表示任意，'*'表示任意数量
if re.match(regex_str,line):
    print('yes')
else:
    print('no')

line = "weiwei123"
regex_str = "^w.*3$" # 匹配以'w'开头的3结尾的任意字符串，'^w'代表w开头, '.'表示任意，'*'表示任意数量, '3$'，代表3结尾
if re.match(regex_str,line):
    print('yes')
else:
    print('no')