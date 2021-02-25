#!/usr/bin/env python   Linux中要声明python的环境变量的位置
# -*- coding:utf-8 -*-  声明编码方式
# @FileName  :3_阶乘之和.py    文件名
# @Time      :2021/1/15 14:14   时间
# @Author    :李世奇   作者
# ########################################################################################################   1--100阶乘和

sum1 = 0
for a in range(1, 100):
    b = 1
    for c in range(1, a+1):
        b = b * c
    sum1 = sum1 + b
print(sum1)



# b = 1
# sum = 0
# for a in range(1, 100):
#     b = b * a
#     sum = sum + b
# print(sum)

