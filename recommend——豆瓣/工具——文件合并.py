import pandas as pd

df1 = pd.read_excel(r'D:\experiment\第三次豆瓣\train\user_id_xy.xls', encoding='gbk')#读取第一个文件

df2 = pd.read_excel(r'D:\experiment\第三次豆瓣\train\user_Cluster_T2=128.xls', encoding='gbk')#读取第二个文件

outfile = pd.merge(df1, df2,  left_on='x-1000', right_on='x_point')#文件合并 left_on左侧DataFrame中的列或索引级别用作键。right_on 右侧


outfile.to_excel(r'D:\experiment\第三次豆瓣\train\user_id_cluster.xls', index=False)#输出文件
