# coding: utf-8
import os
import shutil
m = 83
n = 574
for i in range(22):
    JPG_folder = r"C:\\Users\\Lenovo\\Desktop\\data\\" + str(m)
    Paste_JPG_folder = r"C:\Users\Lenovo\Desktop\image"
    Paste_label_folder = r"C:\Users\Lenovo\Desktop\label"
    #  获取文件夹内的文件名

    FileNameList2 = os.listdir(JPG_folder)
    #  激活labelme环境
    os.system("activate labelme")
    for i in range(len(FileNameList2)):
        #  判断当前文件是否为json文件
        if(os.path.splitext(FileNameList2[i])[1] == ".json"):
            json_file = JPG_folder + "\\" + FileNameList2[i]
            #  将该json文件转为png
            os.system("labelme_json_to_dataset " + json_file)


    #  获取文件夹内的文件名
    FileNameList = os.listdir(JPG_folder)


    for i in range(len(FileNameList)):
        if n >= 0 and n < 10:
            NewFileName = '0000' + str(n)
        elif n >= 10 and n < 100:
            NewFileName = '000' + str(n)
        elif n >= 100 and n < 1000:
            NewFileName = '00' + str(n)
        elif n >= 1000 and n < 10000:
            NewFileName = '0' + str(n)
        #  判断当前文件是否为jpg文件
        if(os.path.splitext(FileNameList[i])[1] == ".jpg"):
            #  复制jpg文件
            JPG_file = JPG_folder + "\\" + FileNameList[i]
            new_JPG_file = Paste_JPG_folder + "\\" + str(NewFileName) + ".png"
            shutil.copyfile(JPG_file, new_JPG_file)
            #  复制label文件
            jpg_file_name = FileNameList[i].split(".", 1)[0]
            label_file = JPG_folder + "\\" + jpg_file_name + "_json\\label.png"
            new_label_file = Paste_label_folder + "\\" + str(NewFileName) + "_mask.png"

            shutil.copyfile(label_file, new_label_file)
            #  文件序列名+1
            n = n + 1
    m = m + 1