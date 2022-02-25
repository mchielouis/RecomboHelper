import numpy as np
import matplotlib.pyplot as plt

numBins = 4
numEvents = 4

histdata=[]
with open('testHis.txt','r') as hist:
	for line in hist:
		histdata.append([int(x) for x in line.strip().split()])

print histdata
histogramSeries = np.array(histdata)
print histogramSeries
fig, ax = plt.subplots()
rects = ax.bar(range(numBins), np.ones(numBins)*10)  # 40 is upper bound of y-axis

for i in range(numEvents):
    [rect.set_height(h) for rect,h in zip(rects,histogramSeries[i,:])]
    fig.canvas.draw()
    plt.pause(1)
