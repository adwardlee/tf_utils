import os
import sys
import subprocess
import shutil
import random
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

file1 = open('/media/llj/storage/msr-vtt/models/data/baseline_test.txt','r')
file2 = open('/media/llj/storage/msr-vtt/models/data/multitask-reinforce_test.txt','r')

file3 = open('/media/llj/storage/msr-vtt/models/data/baseline.txt','w')
file4 = open('/media/llj/storage/msr-vtt/models/data/multitask-reinforce.txt','w')

sents1 = []
sents2 = []
for line in file1:
   line = line.strip()
   id_sent = line.split('\t')
   sents1.append((id_sent[0], id_sent[1]))
   
for line in file2:
   line = line.strip()
   id_sent = line.split('\t')
   sents2.append((id_sent[0], id_sent[1]))


sents1.sort(key=lambda tup: tup[0])
sents2.sort(key=lambda tup: tup[0])

for line in sents1:
    file3.write(line[0])
    file3.write('\t')
    file3.write(line[1])
    file3.write('\n')

for line in sents2:
    file4.write(line[0])
    file4.write('\t')
    file4.write(line[1])
    file4.write('\n')
