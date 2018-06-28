from PIL import ImageFile
import PIL.Image as Image
import math
import os



# 打开文件夹所有图片
def openImg(path):
    print("openImg running")
    if os.path.exists(path):
        print("文件夹已存在")
        os.chdir(path)
        os.getcwd()
    else:
        print("路径出错")

    imgList = os.listdir(os.getcwd())
    return  imgList

# 图片改名字  不可用   img = Image.open(i)打开图片，所以冲突不能修改图片

def changeImgName(path,bgn):
    if os.path.exists(path):
        print("文件夹已存在")
        os.chdir(path)
        os.getcwd()
    else:
        print("路径出错")

    beginName = bgn
    num = 0
    newname = "test"
    newname = newname.strip()

    #要修改的文件的格式
    pic_ext = ['.jpg', '.png']
    for i in os.listdir(path):
        if os.path.isfile(i) == True:
            name, ext = os.path.splitext(i)
            # print (ext)
            if ext in pic_ext:
                num = num+1+beginName
                try:
                    img = Image.open(i)  # 打开图片
                except IOError:
                    print("Error: 没有找到文件或读取文件失败", i)
                else:
                    newname1 = newname + '_' + str(num) + ext
                    # i["ImgName"] = newname1 + ".jpg"
                    os.rename(i,newname1)

                    # img['ImgName']= "name" + ".png"
                    # img.save(savePath)

# 图片重命名 可用
def rename(path):
    ##输入新的文件名
    newname = "a"
    newname = newname.strip()
    if newname != '':
        os.chdir(path)
        ##获取当前文件夹的路径
        path = os.getcwd()
        ##要修改的文件的格式
        pic_ext = ['.jpg', '.png']
        i = 0
        for file in os.listdir(path):
            if os.path.isfile(file) == True:
                name, ext = os.path.splitext(file)
                print (ext)
                if ext in pic_ext:
                    i = i + 1
                    newname1 = newname + '_' + str(i) + ext
                    os.rename(file, newname1)




# 拼接图片
def spliceImg(path):
    if os.path.exists(path):
        print("文件夹已存在")
        os.chdir(path)
        os.getcwd()
    else:
        print("路径出错")

    imgList = os.listdir(os.getcwd())
    numImages = len(imgList)

    eachSize = 32
    eachLine = int(math.sqrt(numImages)) + 1

    toImage = Image.new('RGBA', (eachSize * eachLine, eachSize * eachLine))  # 新建一块画布

    x = 0
    y = 0
    for i in imgList:
        try:
            img = Image.open(i)  # 打开图片
        except IOError:
            print("Error: 没有找到文件或读取文件失败", i)
        else:
            toImage.paste(img, (x * eachSize, y * eachSize))  # 拼接图片


# 缩小图片
def shrinkImg(size, openpath,savepath):
    # if os.path.exists(path):
    #     print("文件夹已存在")
    #     os.chdir(path)
    #     os.getcwd()
    # else:
    #     print("路径出错")
    #
    # imgList = os.listdir(os.getcwd())

    imgList = openImg(openpath)

    # eachSize = size
    for i in imgList:
        try:
            img = Image.open(i)  # 打开图片
        except IOError:
            print("Error: 没有找到文件或读取文件失败", i)
        else:
            print(img.size)
            if img.size[0]>img.size[1]:
                img = img.resize((size, int(img.size[1]/img.size[0]*size)), Image.ANTIALIAS)  # 缩小图片
            else:
                img = img.resize((int(img.size[0]/img.size[1]*size),size), Image.ANTIALIAS)  # 缩小图片

            basename = os.path.basename(i)
            # img = img.resize((width, height), Image.ANTIALIAS)  # 缩小图片
            if basename[-4:] == ".png":
                r, g, b, a = img.split()
                img = Image.merge("RGB", (r, g, b))
                basename = basename[:-4]+".jpg"  #改格式
            img.save(os.path.join(savepath,basename)) #save image



# changeImgName(openPath,0)
# rename(openPath)
openPath = "C:\\Users\\laomingming\\Pictures\\openpath"
savePath = "C:\\Users\\laomingming\\Pictures\\aPythonTest"
path2 = ""
shrinkImg(600,openPath,savePath)