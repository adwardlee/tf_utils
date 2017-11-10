import os
from collections import defaultdict
import collections
import re

path1 = '/media/llj/storage/microsoft-corpus/segments/bianca/first'
path2 = '/media/llj/storage/microsoft-corpus/segments/bianca/fourth'
path3 = '/media/llj/storage/microsoft-corpus/segments/Ryan/first'
path4 = '/media/llj/storage/microsoft-corpus/segments/Ryan/fourth'
path5 = '/media/llj/storage/microsoft-corpus/segments/bianca/all'
path6 = '/media/llj/storage/microsoft-corpus/segments/Ryan/all'


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

videoid = []
for root,subfolders, files in os.walk(path4):
       for filename in files:
                                #print ' filename: ',filename
                                filename = filename[:-4]
                                videoid.append(filename) 
                		

sent_train = defaultdict(list)
with open('sents_train_noval_lc_nopunc.txt','r') as f1:
    for line in f1:
        line = line.strip()
        id_sent = line.split('\t')
        if id_sent[0] in videoid:
            #print ' filename: ',id_sent[0]
            sent_train[id_sent[0]].append(id_sent[1])


with open('ryan_fourth.txt','w') as f2:
     for key in natural_sort(sent_train.keys()):
         for item in sent_train[key]:
             f2.write(key)
             f2.write('\t')
             f2.write(item)
             f2.write('\n')

