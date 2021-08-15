import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

points = []
center_points = []

file="D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\train\\douban_train_zuobiao.csv"
data=pd.read_csv(file)
train_data = np.array(data)#np.ndarray()每个姓名转换为一个list[]
#print(train_data)
all_list=train_data.tolist()#转换list
#print(all_list)

for item in all_list:
    print(item[2])
    print(item[3])
    print("-----------------------")
    point = [item[2], item[3]]
    points.append(point)

#print(type(points))#每个点存入列表
points = np.array(points)#转化为数组形式
print(points)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig, ax = plt.subplots()
for item in points:
    ax.scatter(item[0], item[1], c='red')
plt.title('散点图')
plt.xlabel("X偏好")
plt.ylabel("Y偏好")
plt.show()