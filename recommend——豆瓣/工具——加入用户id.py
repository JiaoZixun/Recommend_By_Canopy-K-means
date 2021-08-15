import pandas as pd
import numpy as np
from pandas import DataFrame,Series


for i in range(1,183,1):
    # 读取清洗后的文件
    file="D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\recommend_处理前\\user_{}_k邻=30_recommend.xls".format(i)
    print(file)
    data = pd.read_excel(file, encoding='utf-8')  # 如果是csv文件则用read_csv
    data[2]=''
    train_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data)
    all_list = train_data.tolist()  # 转换list
    print(all_list)
    for item in all_list:
        item[2]=i
    print(all_list)

    #筛选热门
    file2 = "D:\\experiment\\第三次豆瓣\\豆瓣1500部热门电影.xls"
    data2 = pd.read_excel(file2)
    train_data2 = np.array(data2)  # np.ndarray()每个姓名转换为一个list[]
    # print(train_data2)
    all_list2 = train_data2.tolist()  # 转换list
    print(all_list2)
    remen = []
    for item in all_list2:
        for name in item:
            remen.append(name)
    print(remen)

    test = []
    for item in all_list:
        if item[0] in remen:
            test.append(item)
    print(test)

    data=pd.DataFrame(test)
    outfile="D:\\experiment\\第三次豆瓣\\测试4_K近邻=30\\对比实验\\recommend_加入用户id\\user_{}_k邻=30_recommend.xls".format(i)
    data.to_excel(outfile, index=False)
print("加入完毕")

