import numpy as np
import math
import matplotlib.pyplot as plt
import random








cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, 20)]


words = np.load('num_valid_words.npy')
a = np.load('np_atten.npy') ######### 670 x 35 x 32
x1 = [i+1 for i in xrange(4)]
x = [float(i+1) for i in xrange(32)]#####32
bb = [float(i) for i in xrange(35)]#### 35
aa = [i for i in xrange(670)]#### 670

#a = np.sum(a,axis=1)#### 670 x 32
#a = np.divide(a,words) ### 670 x32 / 670 x1
#quarter1 = np.sum(a[:,:8],1,keepdims=True)##### 670x1
#quarter2 = np.sum(a[:,8:16],1,keepdims=True) #### 670
#quarter3 = np.sum(a[:,16:24],1,keepdims=True)
#quarter4 = np.sum(a[:,24:32],1,keepdims=True)
#args = (quarter1,quarter2,quarter3,quarter4)
#all1 = np.concatenate(args, axis=1) #### 670 x4


quarter1 = np.sum(a[:,:,:8],axis=2) ###### 670 x35
quarter2 = np.sum(a[:,:,8:16],axis=2) ###### 670 x35
quarter3 = np.sum(a[:,:,16:24],axis=2) ###### 670 x35
quarter4 = np.sum(a[:,:,24:32],axis=2) ###### 670 x35

all_words = np.sum(words) ###### words num
print 'all words: ',all_words

a25quarter1 = 0
a50quarter1 = 0
a75quarter1 = 0

a25quarter4 = 0
a50quarter4 = 0
a75quarter4 = 0


for i in np.nditer(quarter1):
    if i > 0.5:
       a50quarter1 += 1
    if i > 0.25:
       a25quarter1 += 1
    if i > 0.75:
       a75quarter1 += 1

for i in np.nditer(quarter4):
    if i > 0.5:
       a50quarter4 += 1
    if i > 0.25:
       a25quarter4 += 1
    if i > 0.75:
       a75quarter4 += 1

print ' 25quarter1: ',a25quarter1
print ' 50quarter1: ',a50quarter1
print ' 75quarter1: ',a75quarter1
print ' 25quarter4: ',a25quarter4
print ' 55quarter4: ',a50quarter4
print ' 75quarter4: ',a75quarter4

#oneline = random.sample(aa,20)
#print ' oneline: ',oneline


#for i in xrange(20):
#    y = all1[oneline[i],:]
#    plt.plot(x1,y,color =colors[i])

#all2 = np.sum(all1,axis=0)/670.0
#print ' all 2 : ', all2
#plt.plot(x1, all2, color='r',linewidth=5.0)
#plt.show()


