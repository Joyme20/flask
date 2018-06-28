# encoding: utf-8
import shutil
from flask import *
import itchat
from PIL import ImageFile
import PIL.Image as Image
import math
import os
# import qrcode
from io import BytesIO
from flask import send_file
from requests import ConnectionError

app = Flask(__name__)


# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.settimeout(CHECK_TIMEOUT)
# sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# sock.bind(('', UDP_PORT))

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/index')
# def index():
#     user = { 'nickname': 'Miguel' } # fake user
#     posts = [ # fake array of posts
#         {
#             'author': { 'nickname': 'John' },
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': { 'nickname': 'Susan' },
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index.html",
#         title = 'Home',
#         user = user,
#         posts = posts)

@app.route('/')
def index():
    return render_template('wx.html')


@app.route('/wx')
def wx():
    itchat.auto_login(hotReload=True)
    # shutil.copy(os.getcwd() + '/' + 'QR.png', '/home/ubuntu/usr/python/untitled/static/QR.png')



    friends = itchat.get_friends(update=True)[0:]
    user = friends[0]["NickName"]

    print(user)

    name = user
    path = 'C:\\Users\\laomingming\\Pictures\\' + name + '/'

    if os.path.exists(path):
        print("文件夹已存在")
    else:
        os.mkdir(path)

    os.chdir(path)
    os.getcwd()
    num = 0

    for i in friends:

        try:

            if os.path.exists(path+i["UserName"]):
                print("文件已存在")

            else:
                i['img'] = itchat.get_head_img(userName=i["UserName"])
                i['ImgName'] = i["UserName"][1:] + ".jpg"
                num += 1
                print(num)

        except ConnectionError:
            print('get ' + i["UserName"][1:] + ' fail')
        fileImage = open(i['ImgName'], 'wb')

        fileImage.write(i['img'])

        fileImage.close()

    # path = 'C:\\Users\laomingming\Pictures\刘卓明朋友头像'

    os.chdir(path)
    os.getcwd()
    imgList = os.listdir(os.getcwd())
    numImages = len(imgList)
    # print('I have ',friendsSum,'friend(s), and I got ',numImages,'image(s)')
    print(' I got ', numImages, 'image(s)')

    eachSize = 32
    eachLine = int(math.sqrt(numImages)) + 1
    # eachLine=30
    print("单个图像边长", eachSize, "像素，一行", eachLine, "个头像，最终图像边长", eachSize * eachLine)

    toImage = Image.new('RGBA', (eachSize * eachLine, eachSize * eachLine))  # 新建一块画布
    x = 0
    y = 0
    for i in imgList:
        try:
            img = Image.open(i)  # 打开图片
        except IOError:
            print("Error: 没有找到文件或读取文件失败", i)
        else:
            img = img.resize((eachSize, eachSize), Image.ANTIALIAS)  # 缩小图片
            # from PIL import ImageFile

            ImageFile.LOAD_TRUNCATED_IMAGES = True
            toImage.paste(img, (x * eachSize, y * eachSize))  # 拼接图片
            x += 1
        if x == eachLine:
            x = 0
            y += 1
    print("图像拼接完成")
    print('1')
    print('toImage:' , type(toImage))

    img = toImage
    print('img:' , type(img))

    # toImage.show()
    # img = toImage.save(r'C:\%s.png' % name)
    # resp = Response(img, mimetype="image/jpeg")
    # return resp

    # return render_template("wx.html",img = resp)
    # return u"data:image/png;base64," + base64.b64encode(img.getvalue()).decode('ascii')
    byte_io = BytesIO()
    print('byte_io:' , type(byte_io))
    img.save(byte_io, 'PNG')
    print('imgsave:' , type(img))
    byte_io.seek(0)
    print('byte_ioseek:' , type(byte_io))
    return send_file(byte_io, mimetype='image/png')

    # return render_template("wx.html",
    #                        title = "老明明|朋友微信头像合成",
    #                        img = resp)
    # close()


if __name__ == '__main__':
    # app.run(host='193.112.14.234', port=14147)
    # app.run(host='0.0.0.0', port=14147)
    app.run(port=14147)
