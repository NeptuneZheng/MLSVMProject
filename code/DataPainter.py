import  matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab as pl
import math


xmajorLocator = MultipleLocator(5)
xminorLocator = MultipleLocator(1)

ymajorLocator = MultipleLocator(10)
yminorLocator = MultipleLocator(1)


with open("data/ml.txt") as ifile:
    xt=[]
    yt=[]

    xf=[]
    yf=[]
    for line in ifile:
        arrs = line.strip().split("*")

        # 1.0show data issue
        if(arrs[0] and arrs[2]=="true"):
            xt.append(arrs[0])
            yt.append(arrs[1])
        else :
            if(arrs[0] and arrs[2]=="false"):
                xf.append(arrs[0])
                yf.append(arrs[1])


plt.figure(1)
ax1 = plt.subplot(1,1,1)
ax1.xaxis.set_major_locator(xmajorLocator)
ax1.xaxis.set_minor_locator(xminorLocator)
ax1.yaxis.set_major_locator(ymajorLocator)
ax1.yaxis.set_minor_locator(yminorLocator)

# 1.0show data issue
pl.scatter(xt,yt,s=40,color="g")
pl.scatter(xf,yf,s=10,color="r")

pl.xlabel("X:Login Date")
pl.ylabel("Y:Login Region")

pl.show()

