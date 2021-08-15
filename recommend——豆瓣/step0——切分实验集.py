import pandas as pd
import numpy as np


data = pd.read_csv("D:\\experiment\\第三次豆瓣\\测试2\\实验原始数据_clear.csv", encoding='gbk')
#print(data)

train=[]
test=[]

for index, row in data.iterrows():
    #print(index)
    if (index+1)% 5:
        train.append(row)
    else:
        test.append(row)

df1=pd.DataFrame(train)
df2=pd.DataFrame(test)
#print(df1.shape())
#print(df2.shape())
df1.to_csv("D:\\experiment\\第三次豆瓣\\测试2\\train\\实验数据_clear.csv", index=False, encoding='utf-8')
df2.to_csv("D:\\experiment\\第三次豆瓣\\测试2\\test\\测试数据_clear.csv", index=False, encoding='utf-8')


