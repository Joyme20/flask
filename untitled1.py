import shutil
from io import BytesIO

import itchat
import os
from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)


@app.route('/wz')
def hello_world():
    # return 'Hello World!'
    # itchat.login(enableCmdQR=2,hotReload=True,picDir='C:\\Users\laomingming\Pictures\\'+'qr.png')
    # img = itchat.login(hotReload=True)
    # shutil.copy(os.getcwd() + '/' + 'QR.png', '/home/mysite/static/QR.png')

    # byte_io = BytesIO()
    # img.save(byte_io, 'PNG')
    # byte_io.seek(0)
    path = 'C:\\Users\\laomingming\\Pictures\\'
    os.chdir(path)
    os.getcwd()

    a = itchat.get_QRuuid()
    byte_io = itchat.get_QR(a)
    # byte_io = BytesIO()
    # img.save(byte_io, 'PNG')
    # byte_io.seek(0)
    # b.seek(0)
    # b = obj.seek(0)
    print (type(byte_io))
    # byte_io = BytesIO()
    # obj.save(byte_io, 'PNG')
    b = byte_io.seek(0)
    print(type(b))
    return send_file(byte_io,mimetype='image/png')
    # return render_template("wx.html",
    #                        title="老明明|朋友微信头像合成",
    #                        img=resp)
    # return 'hello'
    # return render_template("wx.html",
    #                        title="老明明|朋友微信头像合成",
    #
    #                        )


if __name__ == '__main__':
    # app.run(host='193.112.14.234', port=14147)
    # app.run(host='0.0.0.0', port=14147)
    app.run(port=14147)

