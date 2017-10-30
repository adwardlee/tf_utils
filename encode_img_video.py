import os
import numpy as np
import glob
import argparse
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)



parser = argparse.ArgumentParser(description="read frames in folder")
parser.add_argument("-src_dir",type = str, default='/media/llj/storage/microsoft-corpus/youtube_frame_flow')
parser.add_argument("-rgboutfile", type = str, default = './5frame_list.txt')
parser.add_argument("-flowxoutfile", type = str, default = './25flowx_list.txt')
parser.add_argument("-flowyoutfile", type = str, default = './25flowy_list.txt')
parser.add_argument("-rgb_prefix", type = str, default = 'frame_')
parser.add_argument('--flow_x_prefix', type=str, help="prefix of x direction flow images", default='flow_x_')
parser.add_argument('--flow_y_prefix', type=str, help="prefix of y direction flow images", default='flow_y_')
parser.add_argument("-modality", type = str, default = 'rgb')
parser.add_argument("-framenum", type = int, default = 5)
args = parser.parse_args()

src_dir = args.src_dir
#rgboutfile = args.rgboutfile
#train_num = [1:]
stack_depth = 0
if args.modality == 'rgb':
    stack_depth = 1
    rgboutfile = open(args.rgboutfile,'w')
elif args.modality == 'flow':
    stack_depth = 5
    flowxoutfile = open(args.flowxoutfile,'w')
    flowyoutfile = open(args.flowyoutfile,'w')

if not os.path.exists('/media/llj/storage/microsoft-corpus/segments/first_quarter/'):
    os.makedirs('/media/llj/storage/microsoft-corpus/segments/first_quarter/')

if not os.path.exists('/media/llj/storage/microsoft-corpus/segments/second_quarter/'):
    os.makedirs('/media/llj/storage/microsoft-corpus/segments/second_quarter/')

if not os.path.exists('/media/llj/storage/microsoft-corpus/segments/third_quarter/'):
    os.makedirs('/media/llj/storage/microsoft-corpus/segments/third_quarter/')

if not os.path.exists('/media/llj/storage/microsoft-corpus/segments/fourth_quarter/'):
    os.makedirs('/media/llj/storage/microsoft-corpus/segments/fourth_quarter/')

for root,subfolders, filename in os.walk(src_dir):
	subfolders = natural_sort(subfolders)
	for folders in subfolders:
		files = os.listdir(os.path.join(root,folders))
		frame_cnt = 0
		for filenames in sorted(files):				
			if 'frame' in filenames:
				frame_cnt += 1
		#frame_ticks = map(lambda x: x+1, xrange(10))
                quarter = frame_cnt/4
                half_num = frame_cnt/2
                third_q = quarter + half_num
                step = (quarter-1)/(args.framenum)

                output_name1 = '/media/llj/storage/microsoft-corpus/segments/first_quarter/' + folders + '.mp4'
               # output_name2 = '/media/llj/storage/microsoft-corpus/segments/second_quarter/' + folders + '.mp4'
                #output_name3 = '/media/llj/storage/microsoft-corpus/segments/third_quarter/' + folders + '.mp4'
                output_name4 = '/media/llj/storage/microsoft-corpus/segments/fourth_quarter/' + folders + '.mp4'
                os.system('ffmpeg -r 30 ' + ' -start_number '+ str(1) + ' -i ' + os.path.join(root,folders) + '/frame_%06d.jpg' + ' -vframes '+str(quarter) + ' -vcodec mpeg4 ' + output_name1)
                #os.system('ffmpeg -r 30 '+' -start_number '+ str(quarter) + ' -i '+ os.path.join(root,folders) + '/frame_%06d.jpg' + ' -vframes '+str(quarter) + ' -vcodec mpeg4 ' + output_name2)
               # os.system('ffmpeg -r 30 ' + ' -start_number '+ str(half_num) + '-i ' + os.path.join(root,folders) + '/frame_%06d.jpg' + ' -vframes '+str(quarter) + ' -vcodec mpeg4 ' + output_name3)
                os.system('ffmpeg -r 30 ' + ' -start_number '+ str(third_q) + ' -i ' + os.path.join(root,folders) + '/frame_%06d.jpg'  +' -vframes '+str(quarter) + ' -vcodec mpeg4 ' + output_name4)
