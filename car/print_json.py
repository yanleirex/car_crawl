#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: yanleirex
@license: Apache Licence 
@contact: yanleirex@163.com
@site: http://www.phpgao.com
@software: PyCharm
@file: print_json.py
@time: 2016/3/4 8:58
"""

i=0
with open('car.json') as f:
    for line in f:
        i+=1
f.close()
print i

