# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

num = 12
f = open('D:/nutsCloud/MasterLearning/research/ISPA2021/coding/MotivationExp/one_job_res', 'r')
ff = open('D:/nutsCloud/MasterLearning/research/ISPA2021/coding/MotivationExp/dynamic_res_one_job', 'r')
y = []
y_dynamic = []
time_step = []
for i in range(1, 5):
    if i == 1 or i == 3:
        y.append([float(x) for x in f.readline()[1:-2].split(',', num)])
        y_dynamic.append([float(x) for x in ff.readline()[1:-2].split(',', num)])
    elif i == 4:
        time_step = [float(x) for x in f.readline()[1:-2].split(',', num)]
    else:
        f.readline()
# record y[0] and y[1]
# dynamic record y_dynamic[0] and y_dynamic[1]
print(y)
print(y_dynamic)
x_data = [x for x in range(1, num)]
bar_width=0.4
fig, ax = plt.subplots()
plt.grid(True)
plt.xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
plt.ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
plt.title("The influence to time about task out degree(Static vs Dynamic)")  # Add a title to the axes.
plt.bar([xx-0.2 for xx in x_data], y[0], label='Decreased Time(Static)', color='steelblue', alpha=0.8, width=bar_width)
plt.plot(x_data, y[0], 'bo-', ms=5, label='Decreased Time(Static)')
plt.bar([xx+0.2 for xx in x_data], y_dynamic[0], label='Decreased Time(Dynamic)', color='red', alpha=0.8, width=bar_width)
plt.plot(x_data, y_dynamic[0], 'g*-', ms=5, label='Decreased Time(Dynamic)')
#plt.bar(x_data, y_dynamic[0], label='Decreased Time(Dynamic)', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(x_data,y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
plt.legend()
plt.savefig('dynamic_adjust_pic/Figure_1.png')
plt.show()

fig, ax = plt.subplots()
plt.grid(True)
plt.xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
plt.ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
plt.title("The influence to time about task\'s step(Static vs Dynamic)")  # Add a title to the axes.
plt.bar([xx-0.2 for xx in x_data], y[1], label='Decreased Time(Static)', color='steelblue', alpha=0.8, width=bar_width)
plt.plot(x_data, y[1], 'bo-', ms=5, label='Decreased Time(Static)')
plt.bar([xx+0.2 for xx in x_data], y_dynamic[1], label='Decreased Time(Dynamic)', color='red', alpha=0.8, width=bar_width)
plt.plot(x_data, y_dynamic[1], 'g*-', ms=5, label='Decreased Time(Dynamic)')
#plt.bar(x_data, y_dynamic[0], label='Decreased Time(Dynamic)', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(x_data,y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
plt.legend()
plt.savefig('dynamic_adjust_pic/Figure_2.png')
plt.show()

fig, ax = plt.subplots()
plt.grid(True)
plt.xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
y_data = []
y_data2 = []
for i in range(0, len(y[0])):
    y_data.append(y[1][i] / time_step[i])
    y_data2.append(y_dynamic[1][i] / time_step[i])

ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step(Static vs Dynamic)")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
ax.plot(x_data[1:], y_data[1:], 'go-',label='Decreased Time / Memory Consumption(Static)')
ax.plot(x_data[1:], y_data2[1:], 'yo-',label='Decreased Time / Memory Consumption(Dynamic)')
#plt.bar(x_data, y_dynamic[0], label='Decreased Time(Dynamic)', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(x_data,y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
plt.legend()
plt.savefig('dynamic_adjust_pic/Figure_3.png')
plt.show()
