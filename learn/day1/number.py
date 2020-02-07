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


# 数字类型提供了标量存储和直接访问。它是不可更改类型，变更数字的值会生成新的对象
# 型提供了标量存储和直接访问。它是不可更改类型，变更数字的值会生成新的对象，当然开发者不会感觉到对象已经变化。
# 数字类型是数值型数据，支持整型、浮点、布尔类型和复数。数值型即数值数据，用于表示数量，并可以进行数值运算。
# 数值型数据由整数、小数、布尔值和复数组成，分别对应整型类型、浮点类型、布尔类型和复数类型。

# 通过给已创建的数字对象赋予一个新值，可以“变更”一个数值对象。
# 这里所指的“变更”并没有更新该对象的原始数值，而是生成了一个新的数值对象，并返回这个数值对象的引用。
# 前面说过，数值对象是不可改变的对象，当程序更新一个数值对象时，Python会创建一个新的数值对象，并将该数值对象的引用返回给变量。

def intfunc():
    intObj = 123
    intHexObj = 0x123
    intHexNavObj = -0x123
    print(str(intObj) + "类型:" + type(intObj).__name__)
    print(str(intHexObj) + "类型:" + type(intHexObj).__name__)
    print(str(intHexNavObj), "类型:", type(intHexNavObj).__name__)


intfunc()
