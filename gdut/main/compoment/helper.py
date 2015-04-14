# coding: utf-8

import os
import fnmatch


def isValidSno(sno):
    """
    学号格式:男: 31 13 00 0001
            女: 32 13 01 0002
                性别 年纪 00/01 序号
    """
    if not len(sno) == 10:
        return False
    sex = sno[0:2]
    if not (sex == '31' or sex == '32'):
        return False
    year = sno[2:4]
    if not int(year) in range(10, 15):
        return False
    orderPre = sno[4:6]
    if not (orderPre == '00' or orderPre == '01'):
        return False
    order = sno[6:]
    if not int(order) in range(0, 10000):
        return False

    return True


def hasAvatar(imgpath, sno):
    for img in os.listdir(imgpath):
        if fnmatch.fnmatch(img, sno + '.jpg'):
            return True

    return False
