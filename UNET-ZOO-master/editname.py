import os

path = 'D:\\WMH\\png\\'

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

n = 0
m = 0
for i in fileList:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[m]  # os.sep添加系统分隔符

    # 设置新文件名
    if n>=0 and n<10:
        newname = path + os.sep + '0000' + str(n) + '.png'
    elif n>=10 and n<100:
        newname = path + os.sep + '000' + str(n)  +  '.png'
    elif n>=100 and n<1000:
        newname = path + os.sep + '00' + str(n)  + '.png'
    elif n>=1000 and n<10000:
        newname = path + os.sep + '0' + str(n) + '.png'
    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1
    m += 1