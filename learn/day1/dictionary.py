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
# Python 字典
#
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
import util.log as log


def test():
    # 相当于java中的hashmap或者C#的dictionary
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    # 甚至可以把其他的dictionary放进来
    dict["tinydict"] = tinydict
    # 输出键为'one' 的值
    log.info(dict['one'])
    log.info(dict)
    # 输出键为 2 的值
    log.info(dict[2])
    # 输出完整的字典
    log.info(tinydict)
    # 输出所有键
    log.info(tinydict.keys())
    # 输出所有值
    log.info(tinydict.values())


test()
