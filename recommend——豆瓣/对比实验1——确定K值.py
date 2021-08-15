import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  #从preprocessing加载离差标准化模块
from sklearn.cluster import KMeans              #从cluster加载k均值聚类模块
from sklearn.metrics import calinski_harabaz_score

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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


silhouettteScore = []
SSE = []
for i in range(2,10):
    ##构建并训练模型
    kmeans = KMeans(n_clusters = i,random_state=123).fit(points)
    SSE.append(kmeans.inertia_)
    score = silhouette_score(points,kmeans.labels_)
    silhouettteScore.append(score)
#轮廓系数
plt.figure(figsize=(15,6))
plt.plot(range(2,10),silhouettteScore,linewidth=1.5, linestyle="-")
plt.xlabel("K值——簇数量",size=20)
plt.ylabel("轮廓系数",size=20)

plt.show()
#SSE肘部法
plt.plot(range(2,10),SSE,marker="o")
plt.xlabel("K值——簇数量",size=20)
plt.ylabel("簇内误方差SSE",size=20)
plt.show()




