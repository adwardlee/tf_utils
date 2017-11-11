import os
from collections import defaultdict
import collections
import re

path1 = './train_ryan_first.txt'
path2 = './ryan_first_test.txt'
path3 = './train_ryan_fourth.txt'
path4 = './ryan_fourth_test.txt'
path5 = './train_kevin_first.txt'
path6 = './kevin_first_test.txt'
path7 = './train_kevin_fourth.txt'
path8 = './kevin_fourth_test.txt'


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

videoid = []
with open(path5,'r') as f1:
    for line in f1:
        line = line.strip()
        id_sent = line.split('\t')
        videoid.append(id_sent[0])
                		

sent_train = defaultdict(list)
with open(path6,'r') as f1:
    for line in f1:
        line = line.strip()
        id_sent = line.split('\t')
        if id_sent[0] not in videoid:
            print ' filename: ',id_sent[0]
