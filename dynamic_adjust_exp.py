# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

num = 12
base_dir = 'C:/Users/小小冰/Desktop/MasterLearning'
# base_dir = 'D:/nutsCloud/MasterLearning'
f = open(base_dir + '/research/ISPA2021/coding/MotivationExp/sketch_res_one_job', 'r')
ff = open(base_dir + '/research/ISPA2021/coding/MotivationExp/dynamic_res_one_job', 'r')
avg = open(base_dir + '/research/ISPA2021/coding/MotivationExp/dynamic_res_sequence_average_one_job', 'r')
y = []
y_dynamic = []
time_step = []
y_time = []
avg_different_size = []
for i in range(1, 3):
    avg_different_size.append([float(x) for x in avg.readline()[1:-2].split(',', num)])

print('avg: ')
print(avg_different_size)

for i in range(1, 5):
    if i == 1 or i == 3:
        y.append([float(x) for x in f.readline()[1:-2].split(',', num)])
        y_dynamic.append([float(x) for x in ff.readline()[1:-2].split(',', num)])
    elif i == 4:
        line = f.readline()
        time_step = [float(x) for x in line[1:-2].split(',', num)]
        y_time.append([float(x) for x in line[1:-2].split(',', num)])
    else:
        y_time.append([float(x) for x in f.readline()[1:-2].split(',', num)])
        # f.readline()

fixed_memory_dynamic = []
# 0 -> outdegree's decreased time
# 1 -> outdegree's memory size
# 2 -> step's decrease time
# 3 -> step's memory size
for i in range(1, 5):
    fixed_memory_dynamic.append([float(x) for x in ff.readline()[1:-2].split(',', num)])

print(fixed_memory_dynamic)

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
plt.savefig('dynamic_adjust_pic/single_job/Figure_1.png')
# plt.show()

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
plt.savefig('dynamic_adjust_pic/single_job/Figure_2.png')
# plt.show()

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
plt.savefig('dynamic_adjust_pic/single_job/Figure_3.png')
#plt.show()

# show difference about static and dynamic when the memory size is fixed
# outdegree
x_data = [x for x in range(1, num)]
bar_width=0.4
fig, ax = plt.subplots()
plt.grid(True)
ax.set_xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
ax2 = ax.twinx()
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax2.set_ylabel('Memory Consumption')
plt.title("The influence to time and memory consumption \n about task out degree(Static vs Dynamic)")  # Add a title to the axes.
ax2.bar([xx-0.2 for xx in x_data[1:]], y_time[0][1:], label='Mem Consumption(Static)', color='steelblue', alpha=0.8, width=bar_width)
ax.plot(x_data[1:], y[0][1:], 'bo-', ms=5, label='Decreased Time(Static)')
ax2.bar([xx+0.2 for xx in x_data[1:]], fixed_memory_dynamic[1][1:], label='Mem Consumption(Dynamic)', color='red', alpha=0.8, width=bar_width)
ax.plot(x_data[1:], fixed_memory_dynamic[0][1:], 'g*-', ms=5, label='Decreased Time(Dynamic)')
print(y[0])
print(fixed_memory_dynamic[0])
#plt.bar(x_data, y_dynamic[0], label='Decreased Time(Dynamic)', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(x_data,y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
# plt.legend()
ax.legend(loc='upper right')
ax2.legend(loc='upper left')
plt.savefig('dynamic_adjust_pic/single_job/Figure_4.png')
# plt.show()

# step
fig, ax = plt.subplots()
plt.grid(True)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
ax2 = ax.twinx()
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax2.set_ylabel('Memory Consumption')
plt.title("The influence to time and memory consumption \n about task\'s step(Static vs Dynamic)")  # Add a title to the axes.
ax2.bar([xx-0.2 for xx in x_data[1:]], y_time[1][1:], label='Mem Consumption(Static)', color='steelblue', alpha=0.8, width=bar_width)
ax.plot(x_data[1:], y[1][1:], 'bo-', ms=5, label='Decreased Time(Static)')
ax2.bar([xx+0.2 for xx in x_data[1:]], fixed_memory_dynamic[3][1:], label='Mem Consumption(Dynamic)', color='red', alpha=0.8, width=bar_width)
ax.plot(x_data[1:], fixed_memory_dynamic[2][1:], 'g*-', ms=5, label='Decreased Time(Dynamic)')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.savefig('dynamic_adjust_pic/single_job/Figure_5.png')
# plt.show()

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
    y_data2.append(fixed_memory_dynamic[2][i] / fixed_memory_dynamic[3][i])

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
plt.legend(loc='upper right')
plt.savefig('dynamic_adjust_pic/single_job/Figure_6.png')
# plt.show()

# 图7,图8：显示不同顺序task缓存情况的平均值(减少的时间，占据的内存7，时间/内存8)
# 图7
fig, ax = plt.subplots()
plt.grid(True)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
ax2 = ax.twinx()
# y_major_locator=MultipleLocator(10)
# ax.yaxis.set_major_locator(y_major_locator)
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax2.set_ylabel('Memory Consumption')
plt.title("The influence to time and memory consumption \n about task\'s step(Static vs Dynamic_2)")  # Add a title to the axes.
ax2.bar([xx-0.2 for xx in x_data[1:]], y_time[1][1:], label='Mem Consumption(Static)', color='steelblue', alpha=0.8, width=bar_width)
ax.plot(x_data[1:], y[1][1:], 'bo-', ms=5, label='Decreased Time(Static)')
ax2.bar([xx+0.2 for xx in x_data[1:]], avg_different_size[1][1:], label='Mem Consumption(Dynamic_2)', color='red', alpha=0.8, width=bar_width)
print(avg_different_size[1])
ax.plot(x_data[1:], avg_different_size[0][1:], 'g*-', ms=5, label='Decreased Time(Dynamic_2)')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.savefig('dynamic_adjust_pic/single_job/Figure_7.png')
plt.show()

#图8
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
    print(avg_different_size[0][i])
    print('/')
    print(avg_different_size[1][i])
    y_data2.append(avg_different_size[0][i] / avg_different_size[1][i])

ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step(Static vs Dynamic_2)")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
ax.plot(x_data[1:], y_data[1:], 'go-',label='Decreased Time / Memory Consumption(Static)')
ax.plot(x_data[1:], y_data2[1:], 'yo-',label='Decreased Time / Memory Consumption(Dynamic_2)')
#plt.bar(x_data, y_dynamic[0], label='Decreased Time(Dynamic)', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(x_data,y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
plt.legend(loc='upper right')
plt.savefig('dynamic_adjust_pic/single_job/Figure_8.png')
plt.show()
