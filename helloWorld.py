import itchat as itchat
import re

import sys
from flask import Flask, Response

import markdown
import codecs
from flask_cors import *

app = Flask(__name__)

@app.route('/hello')
def hello_world(img):
    # return 'Hello World!'
    QCR = itchat.auto_login(enableCmdQR=2, hotReload=True).format(img)
    # resp = Response(QCR, mimetype="image/jpeg")
    # a = print(type(QCR),type(resp))
    friends = itchat.get_friends(update=True)[0:]
    siglist = []
    nicklist = []
    a = 0
    for i in friends:
        signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d+\w*|[<>/=]")
        signature = rep.sub("", signature)
        siglist.append(signature)
        nickname = i["NickName"]
        nicklist.append(nickname)
        a = a + 1

    text = "".join(siglist)
    return text

@app.route("/1", methods=['GET', ])
def main():
    in_file = "C:\\Users\laomingming\PycharmProjects\\untitled1\咕啦前端规范之CSS.md"

    # name = argv[0]
    # in_file = '%s.md' % (name)

    # out_file = '%s.html' % (name)

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    return html

@app.route("/articles/<name>", methods=['GET', ])
def markdownCss(name):
    in_file = "C:\\Users\laomingming\PycharmProjects\\untitled1\\" + str(name) + ".md"

    # name = argv[0]
    # in_file = '%s.md' % (name)

    # out_file = '%s.html' % (name)

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    return html

@app.route("/3", methods=['GET', ])
def json():
    json = "jsonTest"
    return  json

    # output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    # output_file.write( html)

    # return flask.jsonify(msg="hello world!")
# from bson.objectid import ObjectId
# from mongoengine import *
# @app.route('/img/<oid>/')
# def get_img(oid=None):
#     if oid:
#         proxy = GridFSProxy(grid_id=ObjectId(oid))
#         return Response(proxy.read(),mimetype='image/jpeg')

# @app.route("/image/<imageid>")
# def index(imageid):
#     image = file("丽江/{}.jpg".format(imageid))
#     resp = Response(image, mimetype="image/jpeg")
#     return resp

# @app.route("/")
# def login():
#     return itchat.auto_login(enableCmdQR=2, hotReload=True)



if __name__ == '__main__':
    CORS(app, supports_credentials=True) #解决跨域请求
    app.run()
    # main(sys.argv[0:])

# app = Flask(__name__)
# CORS(app, supports_credentials=True)