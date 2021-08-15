import KMeans
import Canopy
import Visualization
import csv
import random
import numpy as np
import pandas as pd
from sklearn.metrics import calinski_harabaz_score
from sklearn import metrics

points = []
center_points = []
K = 0
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

canopy = Canopy.Canopy(points, t1=100, t2=100)#设定T1和T2，Canopy聚类,T1>T2
canopy_cluster = canopy.find_cluster_by_canopy()#找到canopy簇
for i in canopy_cluster:
    center_points.append(i[0].tolist())#中心点
print("中心点集：", end=" ")
print(center_points)
K = len(center_points)#k值为簇的多少
print("k值为：",K)

kmeans = KMeans.KMeans(points, center_points, K)#K-means聚类
center_points, kmeans_cluster = kmeans.find_cluster_by_kmeans()#找到K-means聚类的簇
#print("更新后的中心点集：", end=" ")
#print(center_points)
for i in kmeans_cluster:
    print(i)

data1 = np.array(center_points)  # np.ndarray()每个姓名转换为一个list[]
data2 = np.array(kmeans_cluster)  # np.ndarray()每个姓名转换为一个list[]
# print(train_data)

visual = Visualization.Visualization(center_points, kmeans_cluster)
visual.visual()


