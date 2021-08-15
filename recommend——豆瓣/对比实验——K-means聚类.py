import numpy as np
import pandas as pd
#from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import xlwt
import KMeans
import Visualization


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

points = []
center_points = []
K = 4
file="D:\\experiment\\第三次豆瓣\\测试3\\train\\douban_train_zuobiao.csv"
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
#print(points)


center_points=[[18.26227416, -42.2997346], [16.23449381, -36.77185165], [58.35130569, 34.61516792], [-4.43906712, -56.93233191]]

kmeans = KMeans.KMeans(points, center_points, K)#K-means聚类
center_points, kmeans_cluster = kmeans.find_cluster_by_kmeans()#找到K-means聚类的簇
for i in kmeans_cluster:
    print(i)
data1 = np.array(center_points)  # np.ndarray()每个姓名转换为一个list[]
data2 = np.array(kmeans_cluster)  # np.ndarray()每个姓名转换为一个list[]
# print(train_data)
visual = Visualization.Visualization(center_points, kmeans_cluster)
visual.visual()





