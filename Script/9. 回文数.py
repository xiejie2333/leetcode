#! python 3.7.9
# -*- coding:utf-8 -*-
# Author:XJ
# Time:2021 2021/7/22 18:46
"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
输入：x = 121
输出：true
"""


def is_palindrome(x):
    str_x = str(x)
    return True if str_x == str_x[::-1] else False


print(is_palindrome(454))