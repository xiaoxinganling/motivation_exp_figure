# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import colorsys
from matplotlib.ticker import MultipleLocator


def _get_colors(num_colors):
    colors=[]
    for i in np.arange(0., 360., 360. / num_colors):
        hue = i/360.
        lightness = (50 + np.random.rand() * 10)/100.
        saturation = (90 + np.random.rand() * 10)/100.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors


base_dir = 'D:/nutsCloud'
odf = open(base_dir + '/MasterLearning/research/ISPA2021/coding/MotivationExp/dynamic_exp/dynamic_res_multiple_job_fixed_size_out_degree', 'r')
sf = open(base_dir + '/MasterLearning/research/ISPA2021/coding/MotivationExp/dynamic_exp/dynamic_res_multiple_job_fixed_size__step', 'r')
sequence_sf = open(base_dir + '/MasterLearning/research/ISPA2021/coding/MotivationExp/dynamic_exp/dynamic_res_multiple_job_sequence_step', 'r')


# data
out_degree_res_time =[]
out_degree_res_mem =[]
step_res_time = []
step_res_mem = []

# sequence
sequence_step_res_time = []
sequence_step_res_mem = []

while odf.readable():
    if len(odf.readline()) == 0:
        break
    out_degree_res_time.append([float(x) for x in odf.readline()[1:-2].split(',')])
    out_degree_res_mem.append([float(x) for x in odf.readline()[1:-2].split(',')])

while sf.readable():
    if len(sf.readline()) == 0:
        break
    step_res_time.append([float(x) for x in sf.readline()[1:-2].split(',')])
    step_res_mem.append([float(x) for x in sf.readline()[1:-2].split(',')])

while sequence_sf.readable():
    if len(sequence_sf.readline()) == 0:
        break
    sequence_step_res_time.append([float(x) for x in sequence_sf.readline()[1:-2].split(',')])
    sequence_step_res_mem.append([float(x) for x in sequence_sf.readline()[1:-2].split(',')])

print(len(out_degree_res_time), len(out_degree_res_mem), len(step_res_time), len(step_res_mem))
colors_od = _get_colors(len(out_degree_res_time))
colors_s = _get_colors(len(step_res_mem))
# 图1：展示不同出度job的time平均值

fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to time about task out degree(Dynamic::fixed memory)")

for i in range(0, len(out_degree_res_time)):
    print("Decreased time-{}".format(str(len(out_degree_res_time[i]))))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(out_degree_res_time[i]) + 1)], out_degree_res_time[i][1:],
            color=colors_od[i], marker='o',
            label="Decreased time-{}".format(str(len(out_degree_res_time[i]))))
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_1_new.png', figsize=(1920,1080), dpi=300)
#plt.show()

# 图2：展示不同出度job的mem平均值

fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
ax.set_ylabel('Memory Consumption For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to memory about task out degree(Dynamic:fixed memory)")

for i in range(0, len(out_degree_res_mem)):
    print("Memory Consumption-{}".format(str(len(out_degree_res_mem[i]))))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(out_degree_res_mem[i]) + 1)], out_degree_res_mem[i][1:],
            color=colors_od[i], marker='o',
            label="Memory Consumption-{}".format(str(len(out_degree_res_mem[i]))))
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_2_new.png')
#plt.show()

# 图3：展示不同step的time平均值
fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to time about task\'s step(Dynamic:fixed memory)")  # Add a title to the axes.

for i in range(0, len(step_res_time)):
    print("Decreased time-{}".format(str(len(step_res_time[i]))))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(step_res_time[i]) + 1)], step_res_time[i][1:],
            color=colors_s[i], marker='o',
            label="Decreased time-{}".format(str(len(step_res_time[i]))))
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_3_new.png')
#plt.show()

# 图4：展示不同step的memory平均值
fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Mem Consumption For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to memory about task\'s step(Dynamic:fixed memory)")  # Add a title to the axes.

for i in range(0, len(step_res_mem)):
    tag = "Mem Consumption-{}".format(str(len(step_res_mem[i])))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(step_res_mem[i]) + 1)], step_res_mem[i][1:],
            color=colors_s[i], marker='o',
            label=tag)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_4_new.png')
#plt.show()

# 图5 展示不同step的缓存性价比
fig, ax = plt.subplots()
y_data = []
for i in range(0, len(step_res_mem)):
    y_tmp = []
    for j in range(0, len(step_res_mem[i])):
        y_tmp.append(step_res_time[i][j] / step_res_mem[i][j])
    y_data.append(y_tmp)
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step(Dynamic:fixed memory)")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
for i in range(0, len(step_res_mem)):
    tag = "Decreased Time / Memory Consumption-{}".format(str(len(step_res_mem[i])))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(3, len(step_res_mem[i]) + 1)], y_data[i][2:],
            color=colors_s[i], marker='o',
            label=tag)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_5_new.png')
#plt.show()


# 图6：展示不同step的time平均值(不同sequence)
fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to time about task\'s step(Dynamic:difference sequence)")  # Add a title to the axes.

for i in range(0, len(sequence_step_res_time)):
    print("Decreased time-{}".format(str(len(sequence_step_res_time[i]))))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(sequence_step_res_time[i]) + 1)], sequence_step_res_time[i][1:],
            color=colors_s[i], marker='o',
            label="Decreased time-{}".format(str(len(sequence_step_res_time[i]))))
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_6_new.png')
#plt.show()

# 图7：展示不同step的memory平均值(不同sequence)
fig, ax = plt.subplots()
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Mem Consumption For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to memory about task\'s step(Dynamic:different sequence)")  # Add a title to the axes.

for i in range(0, len(sequence_step_res_mem)):
    tag = "Mem Consumption-{}".format(str(len(sequence_step_res_mem[i])))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(2, len(sequence_step_res_mem[i]) + 1)], sequence_step_res_mem[i][1:],
            color=colors_s[i], marker='o',
            label=tag)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_7_new.png')
#plt.show()

# 图8 展示不同step的缓存性价比(不同sequence)
fig, ax = plt.subplots()
y_data = []
for i in range(0, len(sequence_step_res_mem)):
    y_tmp = []
    for j in range(0, len(sequence_step_res_mem[i])):
        y_tmp.append(sequence_step_res_time[i][j] / sequence_step_res_mem[i][j])
    y_data.append(y_tmp)
ax.grid(True)
ax.set_yscale("log")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step(Dynamic:different sequence)")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
for i in range(0, len(sequence_step_res_mem)):
    tag = "Decreased Time / Memory Consumption-{}".format(str(len(sequence_step_res_mem[i])))
    color = i ** 3 % 256
    print('#{:02X}{:02F}{:02X}'.format(255 - color, color // 2, color))
    ax.plot([x for x in range(3, len(sequence_step_res_mem[i]) + 1)], y_data[i][2:],
            color=colors_s[i], marker='o',
            label=tag)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('../dynamic_adjust_pic/multi_job/Figure_8_new.png')
plt.show()

# y = []
# # time decrease//out degree
# # memory consumption//out degree
# # time decrease//step
# # memory consumption//step
# out_degree_num = len(y[0])
# step_num = len(y[2])
# out_degree_x = [x for x in range(1, out_degree_num + 1)]
# step_x = [x for x in range(1, step_num + 1)]
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# # ax.plot(x_data,y[0], 'ro-',label='Matrix Factorization')
# # ax.plot(x_data,y1_data,'ro-',label='Matrix Factorization')  # Plot some data on the axes.
# # ax.plot(x_data,y2_data,'b^-',label='Page Rank')
# # ax.plot(x_data,y3_data,'g*-',label='SVD++')
# # ax.plot(x_data,y4_data,'c+-',label='ConnectedComponent')
# # ax.plot(x_data,y5_data,'kx-',label='PregelOperation')
# ax.grid(True)
# ax.set_xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
# ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
# ax.set_title("The influence to time and memory about task out degree")  # Add a title to the axes.
# plt.bar(out_degree_x, y[0], label='Decreased JCT', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(out_degree_x, y[1], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# ax.legend(loc='upper left')
# ax2.legend(loc='upper right')
# plt.savefig('sketch_pic/single_job/Figure_1_new.png')
# plt.show()


# # 图2
# fig, ax = plt.subplots()
# ax.grid(True)
# ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
# ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
# ax.set_title("The influence to time and memory about task\'s step")  # Add a title to the axes.
# plt.bar(step_x, y[2], label='Decreased Time', color='steelblue', alpha=0.8)
# ax2 = ax.twinx()  # this is the important function
# ax2.plot(step_x,y[3], 'ro-',label='Memory Consumption')
# # ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Memory Consumption')
# # ax.legend()
# ax2.legend(loc='upper right')
# ax.legend(loc='upper left')
# plt.savefig('sketch_pic/single_job/Figure_2_new.png')
# plt.show()
#
# # 图3
# fig, ax = plt.subplots()
# y_data = []
# for i in range(0, len(y[2])):
#     y_data.append(y[2][i] / y[3][i])
# ax.grid(True)
# ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
# ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
# ax.set_title("The influence to time and memory about task\'s step")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
# ax.plot(step_x[1:], y_data[1:], 'go-',label='Decreased Time / Memory Consumption')
# ax.legend()
# plt.savefig('sketch_pic/single_job/Figure_3_new.png')
# plt.show()