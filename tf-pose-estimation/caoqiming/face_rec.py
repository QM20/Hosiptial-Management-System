# coding:utf-8

import cv2
import os
import numpy as np


# 1 生成人脸识别数据
#  图像是灰度格式，后缀名.pgm
#  图像是正方形 图像大小要一样 在这里使用200*200
def generate():
    # 加载检测图像中人脸位置的对象， xml文件需要去opencv文件夹里面找， 放到项目里面来引入
    face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_default.xml")
    # 调用本机摄像头
    camera = cv2.VideoCapture(0)
    count = 0
    # 读取摄像头
    while True:
        # 读入 帧
        ret, frame = camera.read()
        # 变为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 检测人脸位置
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # 将图片中人脸位置单独拿出来改变成200*200大小的图片 存入本地 作为数据集
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            cv2.imwrite("./data/%s.pgm" % str(count), f)
            count += 1

        cv2.imshow("camera", frame)
        # 如果按键q就退出 否则等50毫秒
        if cv2.waitKey(50) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


# 读取生成好的数据 在我项目目录下整理好的
def readImages():
    x, y = [], []
    path = "./data/faces/"
    image_file = os.listdir(path)
    image_files = [path + i for i in image_file]
    for file in image_files:
        images = os.listdir(file)
        label = file.split("/")[-1][1:]
        for i in images:
            img = cv2.imread(file + "/" + i, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (200, 200))
            x.append(np.asarray(img, dtype=np.uint8))
            y.append(int(label))

    y = np.asarray(y, dtype=np.int32)
    return x, y


# 检测人脸
def face_rec():
    # 获取数据
    x, y = readImages()

    # 人脸识别的模型
    model = cv2.face.EigenFaceRecognizer_create()
    # fisherfaces算法的模型
    # model = cv2.face.FisherFaceRecognizer_create()
    # LBPH算法的模型
    # model = cv2.face.LBPHFaceRecognizer_create()
    """
    Eigenfaces和Fisherfaces 预测时候产生0到20000的评分
        低于4000 5000 的评分都是相当可靠的
    LBPH 产生评分不同，低于50是可靠的 高于80是不可靠的
    """

    # 训练模型
    model.train(np.asarray(x), np.asarray(y))

    # 开摄像头
    camera = cv2.VideoCapture(0)
    # 加载检测人脸对象
    face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_default.xml")
    while True:
        # 读取当前帧
        read, img = camera.read()
        # 当前帧下检测人脸
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            # 画出人脸
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # 转成灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 拿出人脸部分
            roi = gray[x: x+w, y: y+h]
            try:
                # 更改大小
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                # 进行预测
                params = model.predict(roi)
                # 在图像上写预测结果
                # 1.2是字体大小 2是粗细
                img = cv2.putText(img, str(params[0]), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                # prams是一个二元素列表, 第一个元素是预测结果，第二个元素是得分情况
                print(params)

            except Exception as e:
                print(e)
        cv2.imshow("detect face", img)
        if cv2.waitKey(5) & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 调用摄像头 采集人脸照片数据
    # generate()

    # 检测人脸
    face_rec()