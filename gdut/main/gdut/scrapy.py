# coding:utf-8

import gdutsyslogin
import re
import urllib
import urllib2


def scrapy(sno, storagePath, username, password):
    """抓取图片

    Args:
        sno: 学号
        storagePath: 存储路径
    """
    randomNum = getRandom(username, password)
    status = storageImg(sno, storagePath, randomNum)
    return status

def storageImg(sno, storagePath, randomNum):
    year = sno[2:4]
    url = "http://gdut.eswis.cn/upfiles/{num}/userpic/20{year}/{sno}.jpg".format(num = randomNum, year = year, sno = sno)
    print url
    if checkImgUrlStatus(url):
        print "检查图片路径是否存在"
        urllib.urlretrieve(url, storagePath + '/' + sno + '.jpg')
        return True
    else:
        return False


def checkImgUrlStatus(url):
    try:
        req = urllib2.Request(url)
        urllib2.urlopen(req, timeout=3)
        return True
    except urllib2.HTTPError, e:
        return False

def getRandom(username, password):
    """获取随机数"""
    while True:
        # 登陆
        print "登陆中"
        login = gdutsyslogin.login(username, password)
        result = login.result
        if not result == None:
            break

    return getImgUrlNum(result)

def getImgUrlNum(html):
    """接收登录后HTML过滤出随机数

    Returns:
        返回随机数
    """
    filtImgUrl = re.compile(r'img.*?upfiles\/(\d*)')
    number = filtImgUrl.findall(html)

    return number[0]
