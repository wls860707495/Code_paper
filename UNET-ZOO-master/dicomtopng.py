
import SimpleITK
import pydicom
import numpy as np
import cv2
from tqdm import tqdm
import shutil
import os
path = 'D:\\WMH\\png\\'

def load_patient(src_dir):
    '''
        读取某文件夹内的所有dicom文件
    :param src_dir: dicom文件夹路径
    :return: dicom list
    '''
    files = os.listdir(src_dir)

    slices = []
    for s in files:
        instance = pydicom.read_file(src_dir  + s)
        slices.append(instance)

    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
    return slices

def get_pixels_hu_by_simpleitk(dicom_dir):
    '''
        读取某文件夹内的所有dicom文件
    :param src_dir: dicom文件夹路径
    :return: image array
    '''
    reader = SimpleITK.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    img_array = SimpleITK.GetArrayFromImage(image)
    return img_array

def convert_from_dicom_to_jpg(img, low_window, high_window, save_path):
    lungwin = np.array([low_window * 1., high_window * 1.])
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])  # 归一化
    newimg = (newimg * 255).astype('uint8')  # 将像素值扩展到[0,255]
    org_img = cv2.resize(newimg, (512, 512))
    org_img = cv2.cvtColor(org_img,cv2.COLOR_BAYER_GR2RGB)
    cv2.imwrite(save_path, org_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])



if __name__ == '__main__':
	#dicom文件目录
    dicom_dir = 'D:\\WMH\\static\\'
    # 读取dicom文件的元数据(dicom tags)
    slices = load_patient(dicom_dir)
    print('The number of dicom files : ', len(slices))
    # 提取dicom文件中的像素值
    print(slices[0].filename)
    image = get_pixels_hu_by_simpleitk(dicom_dir)
    for i in tqdm(range(image.shape[0])):
    	#输出png文件目录
        img_path = "D:\\WMH\\png\\" + str(i).rjust(5, '0') + "_i.png"
        shape = image[i].shape
        img_array = np.reshape(image[i], (shape[0], shape[1]))  # 获取array中的height和width
        high = np.max(img_array)
        low = np.min(img_array)
        convert_from_dicom_to_jpg(img_array, low, high, img_path)  # 调用函数，转换成jpg文件并保存到对应的路径
        fileList = os.listdir(path)

    n = 0
    m = 0
    for i in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + fileList[m]  # os.sep添加系统分隔符

        # 设置新文件名
        if n >= 0 and n < 10:
            newname = path + os.sep + '0000' + str(n) + '.png'
        elif n >= 10 and n < 100:
            newname = path + os.sep + '000' + str(n) + '.png'
        elif n >= 100 and n < 1000:
            newname = path + os.sep + '00' + str(n) + '.png'
        elif n >= 1000 and n < 10000:
            newname = path + os.sep + '0' + str(n) + '.png'
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)

        n += 1
        m += 1
    dirlist = os.listdir(path)
    for i in dirlist:
        child = os.path.join('%s/%s' % (path, i))
        if os.path.isfile(child):
            imagename, jpg = os.path.splitext(i)  # 分开文件名和后缀
            shutil.copy(child, os.path.join("D:\\Project\\UNET-ZOO-master\\CT\\val\\", imagename + ".png"))
            # 复制后改为原来图片名称
            # 也可以用shutil.move()
            continue





