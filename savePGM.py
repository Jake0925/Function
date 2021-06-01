import os
import cv2
import glob

write_path = "D:\\Image\\aaa\\"
filelist = glob.glob("D:\\Image\\aaa\\*")

for files in filelist:
	print(os.path.basename(files))
	wfileName = os.path.basename(files)
	wfileName = wfileName[:wfileName.rfind('.')]
	print(wfileName)
	img = cv2.imread(files, 0)
	cv2.imwrite(write_path+wfileName+".pgm",img)