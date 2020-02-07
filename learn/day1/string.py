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
# python的字串列表有2种取值顺序
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头
# 如果要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
# [头下标:尾下标] 获取的子字符串**包含头下标的字符，但不包含尾下标的字符**。
# 加号 + 是连接运算符，星号 * 是重复操作

import util.log as log


# 获取子字符串
def substr(str, start, end, step):
    return str[start:end:step]


# 字符串重复
def repeat(str, times):
    return str * times;


def main():
    var = "123456";
    # 获取子字符串，合理的
    log.info(substr(var, 0, 3, 3));
    # 超出字符串长度，会直接获取字符串
    log.info(substr(var, 0, 10, 2));
    # 获取不了子字符串
    log.info(substr(var, 0, 0, 1));
    # 只获取第一个字符串
    log.info(substr(var, 0, -5, 1));
    log.info("=============================")
    # 字符串重复
    log.info(repeat(var, 10));


main()
