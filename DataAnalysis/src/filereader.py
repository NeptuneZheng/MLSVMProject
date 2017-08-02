import numpy as np
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator = MultipleLocator(10)  # 将x主刻度标签设置为10的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数

def FileReader(filepath):
    file = open(filepath)
    time = []
    Qt = []
    for line in file.readlines()[1:]:
        arr = line.strip().replace("\n","").split("\t")
        if(arr.__len__()>1):
            time.append(float(arr[0]))
            Qt.append(float(arr[1]))



    ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
    plot(time, Qt, 'yo')

    fitting1 = np.polyfit(time,Qt,2)
    fitObj1 = np.poly1d(fitting1)
    print(fitObj1)

    plot(time,fitObj1(time),'r')

    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)

    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)

    # 显示次刻度标签的位置,没有标签文本
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)

    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    # ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    show()



FileReader("../source/source.txt")