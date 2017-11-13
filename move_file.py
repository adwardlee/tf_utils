import os
import sys
import subprocess
import shutil
import random

root_dir = '/media/llj/storage/microsoft-corpus/segments/fourth_quarter/train'
output_dir = '/media/llj/storage/microsoft-corpus/segments/Ryan/all'
output_dir1 = '/media/llj/storage/microsoft-corpus/segments/Ryan/first'
output_dir2 = '/media/llj/storage/microsoft-corpus/segments/Ryan/fourth'
output_dir3 = '/media/llj/storage/microsoft-corpus/segments/Ryan/all'

inputdir = '/media/llj/storage/microsoft-corpus/segments/Ryan/first'
outputdir = '/media/llj/storage/microsoft-corpus/segments/bianca/fourth'


ref = 10000

count = 0

for root, dirs, files in os.walk(root_dir):
    number_of_files = len(os.listdir(root)) 
    if number_of_files > ref:
        while(count < 100):
            chosen_one = random.choice(os.listdir(root))
            file_in_track = root
            file_out_dir = output_dir + '/' + chosen_one

            file_out_dir1 = output_dir1 + '/' + chosen_one
            file_out_dir2 = output_dir2 + '/' + chosen_one
            file_out_dir3 = output_dir3 + '/' + chosen_one

            file_to_copy = file_in_track + '/' + chosen_one
            if (os.path.isfile(file_to_copy) == True):
              if (os.path.isfile(file_out_dir) == False):
                if (os.path.isfile(file_out_dir1) == False):
                  if (os.path.isfile(file_out_dir2) == False):
                    if (os.path.isfile(file_out_dir3) == False):
                     count += 1
                     shutil.copy(file_to_copy,output_dir)
                     print file_to_copy
    else:
        files = os.listdir(inputdir)
        for name in files:
            file_to_copy = root_dir + '/' + name
            #print 'file to copy name : ', file_to_copy
            if (os.path.isfile(file_to_copy) == True):
                     shutil.copy(file_to_copy,outputdir)
                     print file_to_copy
