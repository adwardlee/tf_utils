import argparse
import os
import sys
import math
import cv2
import numpy as np
import multiprocessing
import re
import shutil



parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', type=str, help="video image list",
					default='/media/llj/storage/tvcj/hmdbcnn3_test')
parser.add_argument('--origin_file_dir', type=str, default='/media/llj/storage/hmdb51')

args = parser.parse_args()

txt_files = []
for root, folders, filenames in os.walk(args.data_dir):
    for filename in filenames:
        txt_files.append(str(filename))
print ' 1 ', txt_files[0]


class_name = os.listdir(args.origin_file_dir)
for name in class_name:
    if not os.path.exists(args.data_dir + '/' + name):
       os.makedirs(args.data_dir + '/' + name)

for root, folders, filename in os.walk(args.origin_file_dir):
    for folder in folders:
        folder_dir = os.path.join(root,folder)
        avi_files = os.listdir(folder_dir)
        #print ' avi 1', avi_files[0]
        for txt in txt_files:
            if txt[:-4] in str(avi_files):
               shutil.move(args.data_dir + '/' + txt , args.data_dir + '/' + folder+'/'+txt)
        
