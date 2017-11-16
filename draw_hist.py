import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import matplotlib as mpl

font = {'family' : 'normal',
        #'weight' : 'bold',
        #'fontname':'Times New Roman',
        'size'   : 14}

matplotlib.rc('font', **font)
matplotlib.rcParams['font.sans-serif'] = "Times New Roman"

csfont = {'fontname':'Times New Roman'}
a = (2266/4985.0, 457/4985.0, 52/4985.0)#[1.007,1.025, 1.031, 1.099] # ryan #[1.283, 1.272, 1.397, 1.498] # kevin'full'
b = (2278/4985.0, 514/4985.0, 92/4985.0)#[1.075, 1.105, 1.141, 1.079]#[1.337, 1.354, 1.528, 1.518] # 'first'
#c = [1.013,1.046, 1.251, 1.171]#[0.955, 0.977, 1.187, 1.114] # [1.072, 1.115, 1.315, 1.228]# 'last'


my_xticks = ['>1/4', '>1/2', '>3/4']
#plt.xticks(x, my_xticks)

#plt.plot(x, a, 'b',label = 'full') # plotting x, a separately 
#plt.plot(x, b, 'r', label = 'first quarter') # plotting x, b separately 
#plt.plot(x, c, 'g', label = 'last quarter') # plotting x, c separately 
#plt.legend()
#plt.ylim(ymin=0)  # this line
#plt.show()

ind = np.arange(3)
#bins = [i for i in range(4)] # = [0,10,20,30,40,50,60,70,80,90,100]
#aa , _ = np.histogram(a, bins=bins)
#bb , _ = np.histogram(b, bins=bins)

fig, ax = plt.subplots()
# Normalize the counts by dividing it by the sum:
ax.bar(np.arange(3)+0.9, a, width=0.2, color='b', label='First 1/4')
ax.bar(np.arange(3)+1.1, b, width=0.2, color='y', label='Last 1/4')
#ax.set_xticks(np.arange(10))
#ax.set_xticklabels(age)
ax.set_xticks(np.arange(3)+1)
ax.set_xticklabels(my_xticks)
ax.legend()
ax.set_xlim(0,4)
plt.ylim(0,0.5)  # this line
#plt.show()
plt.savefig('figure2.png',dpi=600)


