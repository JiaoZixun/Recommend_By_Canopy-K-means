import pandas as pd

data = pd.read_csv("D:\\experiment\\第三次豆瓣\\data\\实验原始数据_clear.csv", encoding='gbk')
#print(data)

data.to_csv("D:\\experiment\\第三次豆瓣\\data\\实验数据最终.csv", encoding='gbk')