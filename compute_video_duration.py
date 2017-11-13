import subprocess
import os 
from ffprobe import FFProbe

origin_video_path = '/media/llj/storage/microsoft-corpus/msvd_videos/train'
my_video_path1 = '/media/llj/storage/microsoft-corpus/segments/Ryan/first'
my_video_path2 = '/media/llj/storage/microsoft-corpus/segments/Ryan/fourth'
my_video_path3 = '/media/llj/storage/microsoft-corpus/segments/Ryan/all'
my_video_path4 = '/media/llj/storage/microsoft-corpus/segments/kevin/first'
my_video_path5 = '/media/llj/storage/microsoft-corpus/segments/kevin/fourth'
my_video_path6 = '/media/llj/storage/microsoft-corpus/segments/kevin/all'

#out_file1 = open('ryan_first_time','w')
#out_file2 = open('ryan_fourth_time','w')
#out_file3 = open('ryan_all_time','w')
#out_file4 = open('kevin_first_time','w')
#out_file5 = open('kevin_fourth_time','w')
#out_file6 = open('kevin_all_time','w')
out_file7 = open('all900','w')
videoid = []
videoid1 = []
videoid2 = []
videoid3 = []
videoid4 = []
videoid5 = []
videoid6 = []
videoid7 = []

def getLength(filename):
  #result = subprocess.Popen(["ffprobe", filename],
 #   stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  #return [x for x in result.stdout.readlines() if "Duration" in x]
  time = float(FFProbe(filename).video[0].duration)
  return time

for root,subfolders, files in os.walk(origin_video_path):
       for filename in files:
                                #print ' filename: ',filename
                                filename = os.path.join(root,filename)
                                videoid.append(filename)

for root,subfolders, files in os.walk(my_video_path1):
       for filename in files:
                                #print ' filename: ',filename
                                videoid1.append(filename) 

for root,subfolders, files in os.walk(my_video_path2):
       for filename in files:
                                #print ' filename: ',filename
                                videoid2.append(filename) 

for root,subfolders, files in os.walk(my_video_path3):
       for filename in files:
                                #print ' filename: ',filename
                                videoid3.append(filename) 

for root,subfolders, files in os.walk(my_video_path4):
       for filename in files:
                                #print ' filename: ',filename
                                videoid4.append(filename) 

for root,subfolders, files in os.walk(my_video_path5):
       for filename in files:
                                #print ' filename: ',filename
                                videoid5.append(filename) 

for root,subfolders, files in os.walk(my_video_path6):
       for filename in files:
                                #print ' filename: ',filename
                                videoid6.append(filename) 

videoid7.extend(videoid4)
videoid7.extend(videoid5)
videoid7.extend(videoid6)
#time1 = []
#for line in videoid:
#    for line1 in videoid1:
#        if line1 in line:
#            temp_time = getLength(line)
#            print 'time1 : ', temp_time
#            print ' id : ', line1
#            time1.append((line1[:-4],temp_time ))
#sort_time1 = sorted(time1,key=lambda tup: tup[1])
#for a1 in sort_time1:
#    out_file1.write(a1[0])
#    out_file1.write('\t')
#    out_file1.write(str(a1[1]))
#    out_file1.write('\n')
#print ' out_file1 finished '

#time2 = []
#for line in videoid:
#    for line1 in videoid2:
#        if line1 in line:
#            temp_time = getLength(line)
#            print 'time2 : ', temp_time
#            print ' id : ', line1
#            time2.append((line1[:-4],temp_time ))
#sort_time2 = sorted(time2,key=lambda tup: tup[1])
#for a1 in sort_time2:
#    out_file2.write(a1[0])
#    out_file2.write('\t')
#    out_file2.write(str(a1[1]))
#    out_file2.write('\n')
#print ' out_file2 finished '

#time3 = []
#for line in videoid:
#   for line1 in videoid3:
#      if line1 in line:
#            temp_time = getLength(line)
#            print 'time3 : ', temp_time
#            print ' id : ', line1
#           time3.append((line1[:-4],temp_time ))
#sort_time3 = sorted(time3,key=lambda tup: tup[1])
#for a1 in sort_time3:
#    out_file3.write(a1[0])
#    out_file3.write('\t')
#   out_file3.write(str(a1[1]))
#    out_file3.write('\n')
#print ' out_file3 finished '

#time4 = []
#for line in videoid:
#   for line1 in videoid4:
#       if line1 in line:
#            temp_time = getLength(line)
#            print 'time4 : ', temp_time
#            print ' id : ', line1
#            time4.append((line1[:-4],temp_time ))
#sort_time4 = sorted(time4,key=lambda tup: tup[1])
#for a1 in sort_time4:
#    out_file4.write(a1[0])
#    out_file4.write('\t')
#    out_file4.write(str(a1[1]))
#    out_file4.write('\n')
#print ' out_file4 finished '

#time5 = []
#for line in videoid:
#   for line1 in videoid5:
#       if line1 in line:
#            temp_time = getLength(line)
#            print 'time5 : ', temp_time
#            print ' id : ', line1
#            time5.append((line1[:-4],temp_time ))
#sort_time5 = sorted(time5,key=lambda tup: tup[1])
#for a1 in sort_time5:
#    out_file5.write(a1[0])
#    out_file5.write('\t')
#    out_file5.write(str(a1[1]))
#    out_file5.write('\n')
#print ' out_file5 finished '

#time6 = []
#for line in videoid:
#   for line1 in videoid6:
#       if line1 in line:
#            temp_time = getLength(line)
#            print 'time6 : ', temp_time
#            print ' id : ', line1
#            time6.append((line1[:-4],temp_time ))
#sort_time6 = sorted(time6,key=lambda tup: tup[1])
#for a1 in sort_time6:
#    out_file6.write(a1[0])
#    out_file6.write('\t')
#    out_file6.write(str(a1[1]))
#    out_file6.write('\n')
#print ' out_file6 finished '

time7 = []
for line in videoid:
   for line1 in videoid7:
       if line1 in line:
            temp_time = getLength(line)
            print 'time7 : ', temp_time
            print ' id : ', line1
            time7.append((line1[:-4],temp_time ))
sort_time7 = sorted(time7,key=lambda tup: tup[1])
for a1 in sort_time7:
    out_file7.write(a1[0])
    out_file7.write('\t')
    out_file7.write(str(a1[1]))
    out_file7.write('\n')
print ' out_file7 finished '

#out_file1.close()
#out_file2.close() 
#out_file3.close() 
#out_file4.close() 
#out_file5.close() 
#out_file6.close()
out_file7.close()

