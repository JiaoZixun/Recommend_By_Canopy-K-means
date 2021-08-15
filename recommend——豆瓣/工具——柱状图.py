import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('本文算法', '对比实验')
buy_number_precision = [34.5, 33.02]    #准确率
buy_number_recall = [7.3, 6.63]     #召回率

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))  # 准确率条形图的横坐标
index_female = index_male + bar_width  # 召回率条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_precision, width=bar_width, color='b', label='平均准确率')
plt.bar(index_female, height=buy_number_recall, width=bar_width, color='g', label='平均召回率')

plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, waters, fontsize=25)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('Top-10', fontsize=25)  # 纵坐标轴标题
plt.title('本文算法与对比实验在Top-5下的平均准确率/召回率')  # 图形标题

plt.show()
