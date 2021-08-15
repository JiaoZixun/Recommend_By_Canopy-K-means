import pandas as pd
import numpy as np


file1="D:\\experiment\\第三次豆瓣\\测试3\\test\\测试数据_182名_clear.csv"
data1=pd.read_csv(file1, encoding='gbk')
train_data1 = np.array(data1)#np.ndarray()每个姓名转换为一个list[]
#print(train_data)
all_list1=train_data1.tolist()#转换list
print(all_list1)

file2="D:\\experiment\\第三次豆瓣\\豆瓣1500部热门电影.xls"
data2=pd.read_excel(file2)
train_data2 = np.array(data2)#np.ndarray()每个姓名转换为一个list[]
#print(train_data2)
all_list2=train_data2.tolist()#转换list
print(all_list2)
remen=[]
for item in all_list2:
    for name in item:
        remen.append(name)

print(remen)

test=[]
for item in all_list1:
    if item[2] in remen:
        test.append(item)

print(test)
lieming=["user_id", "movie_id", "movie_name", "category_1", "category_2", "category_3"]
data=pd.DataFrame(columns=lieming, data=test)
data.to_csv("D:\\experiment\\第三次豆瓣\\测试3\\test\\热门_测试数据.csv", index=False, encoding='utf-8')

