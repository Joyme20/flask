# from _cffi_backend import typeof

# import itchat
import PIL;
# import image
import os
import re

import itchat


def imagedawnload():
    friends = itchat.get_friends(update=True)[0:]
    user = friends[0]["PYQuanPin"][0:]
    print(user)
    name = "bigfish"
    path = 'C:\\'+name+'\\'
    # path = 'C:\\微信头像3\\'
    if os.path.exists(path):
        print("文件夹已存在")
    else:
        os.mkdir(path)
    # os.mkdir(path)
    os.chdir(path)
    os.getcwd()
    num = 0
    for i in friends:
        try:
            i['img'] = itchat.get_head_img(userName=i["UserName"])
            i['ImgName']=i["UserName"][1:] + ".jpg"
        except ConnectionError:
            print('get '+i["UserName"][1:]+' fail')
        fileImage=open(i['ImgName'],'wb')
        fileImage.write(i['img'])
        num+=1
        print(num)
        fileImage.close()
    #
    # friendsSum=len(friends)
    # imgList=os.listdir(os.getcwd())
    # numImages=len(imgList)
    # print('I have ',friendsSum,'friend(s), and I got ',numImages,'image(s)')

    #初始化计数器
    male = female = other = 0
    #friends[0]是自己的信息，所以要从friends[1]开始
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other +=1
    #计算朋友总数
    total = len(friends[1:])
    #打印出自己的好友性别比例
    print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
    "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
    "不明性别好友： %.2f%%" % (float(other) / total * 100))


def text():
    friends = itchat.get_friends(update=True)[0:]

    siglist = []
    nicklist = []
    a = 0
    for i in friends:
        signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
        rep = re.compile("1f\d+\w*|[<>/=]")
        signature = rep.sub("", signature)
        siglist.append(signature)
        nickname = i["NickName"]
        nicklist.append(nickname)
        a = a+1

    # for i in range(0,a):
    #     print(nicklist[i]+":"+siglist[i]+"\n" )
    # nicklist[i]+":"
    text = "".join(siglist)
    print(text)
# img = itchat.auto_login(enableCmdQR=2,hotReload=True)
uuid = itchat.get_QRuuid()
byte_io = itchat.get_QR(uuid)
id = itchat.check_login(uuid)
if id ==200:
    web = itchat.web_init
    print(web)
    get = itchat.get_contact()
    print(get)

# print (type(itchat.auto_login(enableCmdQR=2,hotReload=True)))
# text()