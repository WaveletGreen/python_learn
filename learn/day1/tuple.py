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
# Python 元组
#
# 元组是另一个数据类型，类似于 List（列表）。
#
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。


import util.log as log


def test():
    tuple = ('runoob', 786, 2.23, 'john', 70.2)
    tinytuple = (123, 'john')
    # 输出完整元组
    log.info(tuple)
    # 输出元组的第一个元素
    log.info(tuple[0])
    # 输出第二个至第四个（不包含）的元素
    log.info(tuple[1:3])
    # 输出从第三个开始至列表末尾的所有元素
    log.info(tuple[2:])
    # 输出元组两次
    log.info(tinytuple * 2)
    # 打印组合的元组
    log.info(tuple + tinytuple)
    try:
        tuple[2] = 1000  # 元组中是非法应用
    except (Exception):
        log.error("元组中的数据不允许修改")


test()
