# coding:utf-8

from .. import settings
from gdut import scrapy
from . import main
from compoment import helper
from flask import request, render_template, url_for, jsonify, current_app


@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/search', methods = ['POST'])
def search():
    imgUrl = None
    sno = request.form['sno']
    if not helper.isValidSno(sno):
        return jsonify(status = "error", message = "学号格式错误")
    else:
        if not helper.hasAvatar(settings.AVATAR_FOLDER, sno):
            storgePath = settings.AVATAR_FOLDER
            status = scrapy.scrapy(sno, storgePath, \
                current_app.config['USERNAME'], current_app.config['PASSWORD'])
            if not status:
                return jsonify(status = "error", message = "查不到该信息")
            else:
                imgUrl = url_for('static', filename= "img/" + sno + ".jpg")
        else:
            imgUrl = url_for('static', filename="img/" + sno + ".jpg")

    return jsonify(status = "success", imgUrl = imgUrl)
