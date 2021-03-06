# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
base_dir = 'D:/nutsCloud'
f = open(base_dir + '/MasterLearning/research/ISPA2021/coding/MotivationExp/sketch_res_one_job', 'r')
y = []
for i in range(1, 5):
    y.append([float(x) for x in f.readline()[1:-2].split(',')])
# time decrease//out degree
# memory consumption//out degree
# time decrease//step
# memory consumption//step
out_degree_num = len(y[0])
step_num = len(y[2])
out_degree_x = [x for x in range(1, out_degree_num + 1)]
step_x = [x for x in range(1, step_num + 1)]
fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot(x_data,y[0], 'ro-',label='Matrix Factorization')
# ax.plot(x_data,y1_data,'ro-',label='Matrix Factorization')  # Plot some data on the axes.
# ax.plot(x_data,y2_data,'b^-',label='Page Rank')
# ax.plot(x_data,y3_data,'g*-',label='SVD++')
# ax.plot(x_data,y4_data,'c+-',label='ConnectedComponent')
# ax.plot(x_data,y5_data,'kx-',label='PregelOperation')
ax.grid(True)
ax.set_xlabel('OutDegree Of Cached Task')  # Add an x-label to the axes.
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task out degree")  # Add a title to the axes.
plt.bar(out_degree_x, y[0], label='Decreased JCT', color='steelblue', alpha=0.8)
ax2 = ax.twinx()  # this is the important function
ax2.plot(out_degree_x, y[1], 'ro-',label='Memory Consumption')
# ax2.set_xlim([0, np.e])
ax2.set_ylabel('Memory Consumption')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.savefig('sketch_pic/single_job/Figure_1_new.png')
plt.show()


# 图2
fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Time Decreased For Caching')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step")  # Add a title to the axes.
plt.bar(step_x, y[2], label='Decreased Time', color='steelblue', alpha=0.8)
ax2 = ax.twinx()  # this is the important function
ax2.plot(step_x,y[3], 'ro-',label='Memory Consumption')
# ax2.set_xlim([0, np.e])
ax2.set_ylabel('Memory Consumption')
# ax.legend()
ax2.legend(loc='upper right')
ax.legend(loc='upper left')
plt.savefig('sketch_pic/single_job/Figure_2_new.png')
plt.show()

# 图3
fig, ax = plt.subplots()
y_data = []
for i in range(0, len(y[2])):
    y_data.append(y[2][i] / y[3][i])
ax.grid(True)
ax.set_xlabel('Task\'s Step From End Task')  # Add an x-label to the axes.
ax.set_ylabel('Decreased Time / Memory Consumption')  # Add a y-label to the axes.
ax.set_title("The influence to time and memory about task\'s step")  # Add a title to the axes.ax2 = ax.twinx()  # this is the important function
ax.plot(step_x[1:], y_data[1:], 'go-',label='Decreased Time / Memory Consumption')
ax.legend()
plt.savefig('sketch_pic/single_job/Figure_3_new.png')
plt.show()