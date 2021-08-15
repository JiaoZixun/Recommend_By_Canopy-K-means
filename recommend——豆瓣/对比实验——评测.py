import math
from operator import *
import pandas as pd
import numpy as np
import xlwt
import csv
import collections

def handle():
    return None
dic1={}#放推荐列表的字典
dic2={}#放真实观影记录
if __name__ == '__main__':
    file1 = "D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\热门_推荐结果_K-means.csv"#推荐结果
    tmp_lst = []
    with open(file1, 'r', encoding='gbk', errors='ignore') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp_lst.append(row)
    data1 = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0])
    #print(data1)

    train_data1 = np.array(data1)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list1 = train_data1.tolist()  # 转换list
    # print(all_list)
    for item in all_list1:
        # print(item)
        dic1.setdefault(int(item[2]), []).append(item[0])  # 将电影名加入对应用户的字典内，键为用户名，值为电影列表
        #这里的用户id读进来是str型需要强制转换为int型与dic2保持一致，并且方便后续用键取值
    print(dic1)


    file2 = "D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\test\\热门_测试数据.csv"
    data2=pd.read_csv(file2, encoding='gbk')
    #print(data2)

    train_data2 = np.array(data2)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list2 = train_data2.tolist()  # 转换list
    # print(all_list)
    for item in all_list2:
        # print(item)
        dic2.setdefault(item[0], []).append(item[2])  # 将电影名加入对应用户的字典内，键为用户名，值为电影列表
    print(dic2)
    precision_all=0
    recall_all=0
    all_num = 0
    for i in range(1,183,1):
        R_num=0
        T_num=0
        R_T=0
        if dic2.get(i) and dic1.get(i) is not None:
            all_num += 1
            for item in dic2[i]:#真实记录列表
                T_num+=1
            for item1 in dic1[i]:#推荐列表
                R_num+=1
                if item1 in dic2[i]:
                    R_T+=1
                if R_num == 25:
                    break
        else:
            continue
        precision = R_T/R_num*1.0
        recall = R_T/T_num*1.0
        print("第", i, "位用户的推荐准确率为：", precision, "召回率为：", recall, "一共中了：", R_T)

        precision_all+=precision
        recall_all+=recall
    precision_all/=all_num
    recall_all/=all_num
    print("平均推荐准确率为：", precision_all, "平均召回率为：", recall_all)
    #print("测试人数：", num, "准确率：", precision_test, "召回率：", recall_test)
    #改变每位用户推荐列表的N值
