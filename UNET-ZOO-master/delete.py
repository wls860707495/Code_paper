#Python简单删除目录下文件以及文件夹
import os
import shutil
filelist=[]
filelist2=[]
filelist3=[]
filelist4=[]

rootdir4 = r"D:\\WMH\\static\\"
rootdir3 = r"D:\\WMH\\png\\"
rootdir2 = r"D:\\Project\\UNET-ZOO-master\\CT\\val\\"
rootdir=r"D:\\Project\\UNET-ZOO-master\\saved_predict\\resnet34_unet\\6\\40\\esophagus\\"                       #选取删除文件夹的路径,最终结果删除img文件夹
filelist=os.listdir(rootdir)                #列出该目录下的所有文件名
for f in filelist:
    filepath = os.path.join( rootdir, f )   #将文件名映射成绝对路劲
    if os.path.isfile(filepath):            #判断该文件是否为文件或者文件夹
        os.remove(filepath)                 #若为文件，则直接删除
        print(str(filepath)+" removed!")
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath,True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
        print("dir "+str(filepath)+" removed!")
filelist2=os.listdir(rootdir2)                #列出该目录下的所有文件名
for f in filelist2:
    filepath2 = os.path.join( rootdir2, f )   #将文件名映射成绝对路劲
    if os.path.isfile(filepath2):            #判断该文件是否为文件或者文件夹
        os.remove(filepath2)                 #若为文件，则直接删除
        print(str(filepath2)+" removed!")
    elif os.path.isdir(filepath2):
        shutil.rmtree(filepath2,True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
        print("dir "+str(filepath2)+" removed!")
filelist3=os.listdir(rootdir3)                #列出该目录下的所有文件名
for f in filelist3:
    filepath3 = os.path.join( rootdir3, f )   #将文件名映射成绝对路劲
    if os.path.isfile(filepath3):            #判断该文件是否为文件或者文件夹
        os.remove(filepath3)                 #若为文件，则直接删除
        print(str(filepath3)+" removed!")
    elif os.path.isdir(filepath3):
        shutil.rmtree(filepath3,True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
        print("dir "+str(filepath3)+" removed!")
filelist4=os.listdir(rootdir4)                #列出该目录下的所有文件名
for f in filelist4:
    filepath4 = os.path.join( rootdir4, f )   #将文件名映射成绝对路劲
    if os.path.isfile(filepath4):            #判断该文件是否为文件或者文件夹
        os.remove(filepath4)                 #若为文件，则直接删除
        print(str(filepath4)+" removed!")
    elif os.path.isdir(filepath4):
        shutil.rmtree(filepath4,True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
        print("dir "+str(filepath4)+" removed!")