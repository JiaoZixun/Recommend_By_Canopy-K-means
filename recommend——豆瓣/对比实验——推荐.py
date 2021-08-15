# -*- coding=utf-8 -*-
import math
from operator import *
import pandas as pd
import numpy as np


def creat_user_cluster(cluster_num):
    file = "D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\对比实验_user_id_Cluster_K=4.xls"
    data = pd.read_excel(file, encoding='utf-8')
    train_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list = train_data.tolist()  # 转换list
    #print(all_list)
    clu=[]
    for item in all_list:
        if cluster_num==item[1]:
            clu.append(int(item[0]))
    return clu

def find_Cluster(userid):
    file = "D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\对比实验_user_id_Cluster_K=4.xls"
    data = pd.read_excel(file, encoding='utf-8')
    train_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list = train_data.tolist()  # 转换list
    #print(all_list)
    for item in all_list:
        if userid == item[0]:
            return item[1]

def creat_user_movie_dic(cluster):
    dic={}
    file = "D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\train\\实验数据_clear.csv"
    data = pd.read_csv(file, encoding='utf-8')
    train_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list = train_data.tolist()  # 转换list
    # print(all_list)
    for item in all_list:
        if item[0] in cluster:
            #print(item[0])
            dic.setdefault(item[0], []).append(item[2])#将电影名加入对应用户的字典内，键为用户名，值为电影列表
    return dic


def Usersim(dicc):
    # 把用户-电影字典转成电影-用户字典
    item_user = dict()#创建一个字典
    #建立倒排表
    for u, items in dicc.items():
        for i in items:  # 不带评分的，所以用的是元组而不是嵌套字典。
            if i not in item_user.keys():
                item_user[i] = set()  # i键所对应的值是一个集合（不重复）。
            item_user[i].add(u)  # 向集合中添加用户。
    #print(item_user)
    C = dict()  # 这里是字符，这边还用字典。
    N = dict()
    for item, users in item_user.items():
        for u in users:
            if u not in N.keys():
                N[u] = 0  # 设定字典初始值
            N[u] += 1  # 每个电影下用户出现一次就加一次，就是计算每个用户一共观看电影次数。
            # 但是这个值也可以从最开始的用户表中获得。
            # 比如： for u in dic.keys():
            #             N[u]=len(dic[u])
            for v in users:
                if u == v:
                    continue
                if (u, v) not in C.keys():  # 同上，没有初始值不能+=
                    C[u, v] = 0
                C[u, v] += 1
    # 到这里倒排阵就建立好了，下面是计算相似度。
    W = dict()
    for co_user, cuv in C.items():
        W[co_user] = cuv / math.sqrt(N[co_user[0]] * N[co_user[1]])
    return W


def Recommend(user, dicc, W2, K):
    rvi = 1  # 这里都是1,实际中可能每个用户就不一样了。
    rank = dict()
    related_user = []
    interacted_items = dicc[user]
    for co_user, item in W2.items():
        if co_user[0] == user:
            related_user.append((co_user[1], item))  # 先建立一个和待推荐用户兴趣相关的所有的用户列表。
    for v, wuv in sorted(related_user, key=itemgetter(1), reverse=True)[0:K]:
        # 找到K个相关用户以及对应兴趣相似度，按兴趣相似度从大到小排列。itemgetter要导包。
        for i in dicc[v]:
            if i in interacted_items:
                continue
            if i not in rank.keys():
                rank[i] = 0
            rank[i] += wuv * rvi
    return rank


if __name__ == '__main__':
    file="D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\对比实验_user_id_Cluster_K=4.xls"
    data=pd.read_excel(file, encoding='utf-8')
    #print(data)
    for i in range(1,183,1):#用户id
        dic = {}
        cluster=[]
        cluster_num=find_Cluster(i)#找到用户在哪个簇
        #print(cluster_num)
        cluster=creat_user_cluster(cluster_num)#创建该簇
        #print(cluster)
        dic=creat_user_movie_dic(cluster)#根据用户簇创建用户电影字典
        #print(dic)
        W3 = Usersim(dic)  # 建立倒排表
        #print(W3)
        Last_Rank = Recommend(i, dic, W3, 30)  # 得到推荐列表
        # print(Last_Rank)
        d_order = sorted(Last_Rank.items(), key=lambda x: x[1],
                         reverse=True)  # 按字典集合中，每一个元组的第二个元素排列。reverse=True为从大到小排序
        print(d_order)  # 排序后的推荐列表
        outfile="D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\recommend_处理前\\user_{}_k邻=30_recommend.xls".format(i)
        outcome=pd.DataFrame(d_order)
        outcome.to_excel(outfile,index=False)
        #break
print("推荐完毕！")


