## Use Yolo Environment
import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
import numpy as np
#import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import cv2
import glob
from tqdm import tqdm
from barcode import EAN13
from barcode.writer import ImageWriter

## Video Path
video_path = r'D:\Raw_Data\data_boxes_with_pallet\pallet_video\vid_pallet_01_13sec.mp4'
address_path = 'D:\\Raw_Data\\data_boxes_with_pallet\\Photo_of_Pallete\\'

#The core process

cap = cv2.VideoCapture(video_path)

i = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    #prevent infinite looping
    if (ret == False):
        break

    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite(address_path+'Framev1'+str(i)+'.jpg',frame)

    i+=1








