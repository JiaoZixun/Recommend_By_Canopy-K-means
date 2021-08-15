#coding=utf-8
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd


points = []

data = pd.read_csv("D:\\experiment\\第三次豆瓣\\测试3\\train\\douban_user_category.csv", encoding='gbk')
train_data = np.array(data)#np.ndarray()每个姓名转换为一个list[]
#print(train_data)
all_list=train_data.tolist()#转换list
#print(all_list)

for item in all_list:
    point = [item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28],
             item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36]]
    points.append(point)

#print(type(points))#每个点存入列表
points = np.array(points)#转化为数组形式
#print(points)

pca = PCA(n_components=2)   #降到2维
pca.fit(points)                  #训练
newPoints=pca.fit_transform(points)   #降维后的数据
# PCA(copy=True, n_components=2, whiten=False)
print("前两维的贡献率分别为：", pca.explained_variance_ratio_)  #输出贡献率
print("-----------------------")
print(newPoints)                  #输出降维后的数据
zuobiao = pd.DataFrame(newPoints)
zuobiao.to_csv('D:\\experiment\\第三次豆瓣\\测试3\\train\\douban_train_zuobiao.csv', index=False,encoding='utf-8')


