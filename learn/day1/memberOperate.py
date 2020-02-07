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
# 成员运算符
# 运算符	逻辑表达式	描述	实例
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

import util.log as log


def memberOperate():
    a = 10
    b = 20

    if a and b:
        log.info("1 - 变量 a 和 b 都为 true")
    else:
        log.info(
            "1 - 变量 a 和 b 有一个不为 true")

    if a or b:
        log.info(
            "2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        log.info(
            "2 - 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if a and b:
        log.info(
            "3 - 变量 a 和 b 都为 true")
    else:
        log.info(
            "3 - 变量 a 和 b 有一个不为 true")

    if a or b:
        log.info(
            "4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        log.info(
            "4 - 变量 a 和 b 都不为 true")

    if not (a and b):
        log.info(
            "5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        log.info("5 - 变量 a 和 b 都为 true")


memberOperate()
