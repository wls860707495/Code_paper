
import os
import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
Paste_label_folder = r"C:\\Users\\Lenovo\\Desktop\\lab\\"
FileNameList2 = os.listdir(Paste_label_folder)
for i in range(len(FileNameList2)):
    img = cv2.imread(Paste_label_folder+FileNameList2[i])
    info = img.shape
    height = info[0]
    width = info[1]
    print(info)
    # dst = np.zeros((height, width, 3), np.uint8)

    # for h in range(height):
    #     for j in range(width):
    #         if any(img[h,j]==38):
    #             img[h,j]=255
    #         dst[h, j] = img[h, j]
    #
    # cv2.imwrite(FileNameList2[i], dst)
