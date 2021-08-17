# 基于Canopy+K-means聚类的豆瓣电影推荐



## 数据

> 所有数据全部来源于豆瓣网站，使用selenium+chromedriver进行爬取

[[基于聚类的推荐算法笔记二](https://blog.csdn.net/jiaoooooo/article/details/119045527)]

爬取数据为（共193205条，0号文件）：

![1](https://github.com/JiaoZixun/Recommend_By_Canopy-K-means/blob/main/img/1.jpg)

清除0号文件username、rating、index、movie_url、Average_score列，然后在类型三列中空白位插入‘#’号占位，最后得到清理后的原始数据：

![2](D:\GitHub_混合聚类推荐算法\img\2.jpg)

### 1.step0

使用step0.py文件划分实验集和测试集。

## 思路

> 通过统计每个用户对各个类别电影的观影数量计算占比得到用户偏好向量，降维之后进行聚类在簇内推荐

### 2.step1

在step1.py中读入实验集，输出统计每位用户观看不同类型的数量：

![3](D:\GitHub_混合聚类推荐算法\img\3.jpg)

第i行表示用户u看过不同类别的电影数量，通过execl文件计算每个类别的占比：

![4](D:\GitHub_混合聚类推荐算法\img\4.jpg)

### 3.step2

step2.py读入该文件进行降维生成坐标点：

![5](D:\GitHub_混合聚类推荐算法\img\5.jpg)

对每个坐标点放大1000倍得到：

![6](D:\GitHub_混合聚类推荐算法\img\6.jpg)

### 4.step3

计算Canopy聚类中的T值，读入坐标点计算每个点到其他点的平均距离的平均值作为T的参考，实验中选择T为100

### 5.step4

进行Canopy+K-means聚类，读入坐标点，在Visualization.py中输出聚类图片和用户聚类关系：

![7](D:\GitHub_混合聚类推荐算法\img\7.jpg)

使用工具——合并聚类和用户id，利用坐标点确定一个用户id将其合并：

![8](D:\GitHub_混合聚类推荐算法\img\8.jpg)

### 6.step5

共有182名用户分别进行推荐，存入文件夹：

![9](D:\GitHub_混合聚类推荐算法\img\9.jpg)

使用工具——加入用户id，在推荐结果中加入用户id：

![10](D:\GitHub_混合聚类推荐算法\img\10.jpg)

使用工具——文件夹合并，将所有推荐结果合并：

![11](D:\GitHub_混合聚类推荐算法\img\11.jpg)

### 7.step6

读入推荐结果和测试集进行对比，得到平均准确率和召回率，改变Top-N推荐N值得到不同准确率和召回率：

![本文算法平均准确率和召回率](D:\GitHub_混合聚类推荐算法\img\本文算法平均准确率和召回率.jpg)



## 改进

> **由于推荐结果数量太大，可以找到豆瓣近几年的热门电影集合，取推荐结果和热门电影集合的交集作为最后推荐结果，测试集也需要和热门电影集合取交集然后进行对比，可以提高准确率。**

## 聚类

> 使用Canopy+K-means混合聚类，点间距离用欧式距离公式计算得到

![Canopy+K-means聚类T1=100,T2=100，K=4](D:\GitHub_混合聚类推荐算法\img\Canopy+K-means聚类T1=100,T2=100，K=4.png)

[[基于聚类的推荐算法笔记一](https://blog.csdn.net/jiaoooooo/article/details/119045349)]

## 推荐

> 使用协同过滤推荐，用户间相似度用余弦公式计算得到

[[基于聚类的推荐算法笔记三](https://blog.csdn.net/jiaoooooo/article/details/119573288)]

## 评价

![本文算法平均准确率和召回率](D:\GitHub_混合聚类推荐算法\img\本文算法平均准确率和召回率.jpg)

[[基于聚类的推荐算法笔记四](https://blog.csdn.net/jiaoooooo/article/details/119573497)]
