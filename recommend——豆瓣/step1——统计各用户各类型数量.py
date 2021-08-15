from pandas import DataFrame
import csv
import xlwt
import pandas as pd
import numpy as np


data = pd.read_csv("D:\\experiment\\第三次豆瓣\\测试3\\train\\实验数据_clear.csv")
#print(data)

#二维矩阵存每个用户观看不同类别的数量
namedic={"其他": 0, "剧情": 1,"喜剧": 2,"动作": 3,"爱情": 4,"科幻": 5,"动画": 6,"悬疑": 7,"惊悚": 8,"恐怖": 9,"犯罪": 10,"传记": 11,"历史": 12,"战争": 13,"西部": 14,"奇幻": 15,"冒险": 16,"纪录片": 17,"武侠": 18,"#": 19}
user_movie_list = np.zeros((182,20))
print(user_movie_list)
i=0
j=0
for index, row in data.iterrows():
    #print(index) # 输出每行的索引值
    #print(row[0])
    if row[0] == i+1:
        user_movie_list[i][namedic.get(row[3], 0)] += 1
        user_movie_list[i][namedic.get(row[4], 0)] += 1
        user_movie_list[i][namedic.get(row[5], 0)] += 1
    else:
        i+=1
        if row[0] == i + 1:
            user_movie_list[i][namedic.get(row[3], 0)] += 1
            user_movie_list[i][namedic.get(row[4], 0)] += 1
            user_movie_list[i][namedic.get(row[5], 0)] += 1
print(user_movie_list)
lieming=["其他","剧情","喜剧","动作","爱情","科幻","动画","悬疑","惊悚","恐怖","犯罪","传记","历史","战争","西部","奇幻","冒险" ,"纪录片","武侠","#"]
user_category = pd.DataFrame(columns=lieming,data=user_movie_list)
user_category.to_csv('D:\\experiment\\第三次豆瓣\\测试3\\train\\douban_user_category.csv', index=False,encoding='utf-8')#输出文件