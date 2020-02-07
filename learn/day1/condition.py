#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fancyears'
__mtime__ = '2020/2/7'
# code is far away from bugs with the god animal protecting
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


# Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

def conditionSimple():
    flag = False
    name = 'luren'
    if name == 'python':  # 判断变量是否为 python
        flag = True  # 条件成立时设置标志为真
        print('welcome boss')  # 并输出欢迎信息
    else:
        print(name)  # 条件不成立时输出变量名称

    if name:
        print("name")
    else:
        print("null")


# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功

def conditionOr():
    num = 9
    if num >= 0 and num <= 10:  # 判断值是否在0~10之间
        print('hello')
    # 输出结果: hello

    num = 10
    if num < 0 or num > 10:  # 判断值是否在小于0或大于10
        print('hello')
    else:
        print('undefine')
    # 输出结果: undefine

    num = 8
    # 判断值是否在0~5或者10~15之间
    if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
        print('hello')
    else:
        print('undefine')
    # 输出结果: undefine


conditionSimple()
conditionOr()
