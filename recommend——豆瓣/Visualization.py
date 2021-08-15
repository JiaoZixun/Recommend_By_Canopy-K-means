import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xlwt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class Visualization:
    center_points = []
    kmeans_cluster = []

    def __init__(self, center_points, kmeans_cluster):
        self.center_points = center_points
        self.kmeans_cluster = kmeans_cluster

    def format_point(self):
        lenth = len(self.kmeans_cluster)
        x_center_point = []
        y_center_point = []
        x_points = [[] for _ in range(lenth)]
        y_points = [[] for _ in range(lenth)]
        for center_point in self.center_points:
            x_center_point.append(center_point[0])
            y_center_point.append(center_point[1])
        for points in range(lenth):
            for point in self.kmeans_cluster[points]:
                x_points[points].append(point[0])
                y_points[points].append(point[1])
        return x_center_point, y_center_point, x_points, y_points

    def visual(self):
        x_center_point, y_center_point, x_point, y_point = self.format_point()
        fig, ax = plt.subplots()
        #colors = ['#F0F8FF', '#FAEBD7', '#00FFFF', '#7FFFD4', '#F0FFFF','#F5F5DC','#FFE4C4','#000000','#FFEBCD','#0000FF','#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E','#FF7F50','#6495ED','#FFF8DC',
        #'#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B', '#A9A9A9','#006400','#BDB76B','#8B008B','#556B2F','#FF8C00','#9932CC','#8B0000','#E9967A','#8FBC8F','#483D8B','#2F4F4F','#00CED1','#9400D3','#FF1493','#00BFFF',
        #'#696969','#1E90FF','#B22222','#FFFAF0','#228B22','#FF00FF','#DCDCDC','#F8F8FF','#FFD700','#DAA520','#808080','#008000','#ADFF2F','#F0FFF0','#FF69B4','#CD5C5C','#4B0082','#FFFFF0',]

        colors = ['#008080','#D8BFD8','#FF6347','#40E0D0','#ADFF2F','#20B2AA','#87CEFA','#F0FFF0','#FF69B4','#EE82EE','#F5DEB3','#FFFFFF','#F5F5F5','#F0F8FF','#FAEBD7','#00FFFF','#7FFFD4','#F0FFFF','#F5F5DC','#FFE4C4','#000000','#FFEBCD','#0000FF','#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E',
                  '#FF7F50','#6495ED','#FFF8DC','#DC143C','#00FFFF','#00008B','#008B8B','#B8860B', '#A9A9A9','#006400','#BDB76B','#8B008B','#556B2F','#FF8C00','#9932CC','#8B0000',
                  '#E9967A','#8FBC8F','#483D8B','#2F4F4F','#00CED1','#9400D3','#FF1493','#00BFFF','#696969','#1E90FF','#B22222','#FFFAF0','#228B22','#FF00FF','#DCDCDC','#F8F8FF',
                  '#FFD700','#DAA520','#808080','#008000','#CD5C5C','#4B0082','#FFFFF0','#F0E68C','#E6E6FA','#FFF0F5','#7CFC00','#FFFACD','#ADD8E6',
                  '#F08080','#E0FFFF','#FAFAD2','#90EE90','#D3D3D3','#FFB6C1','#FFA07A','#778899','#B0C4DE','#FFFFE0', '#00FF00','#32CD32','#FAF0E6','#FF00FF',
                  '#800000','#66CDAA','#0000CD','#BA55D3','#9370DB','#3CB371','#7B68EE','#00FA9A','#48D1CC','#C71585','#191970','#F5FFFA','#FFE4E1','#FFE4B5','#FFDEAD','#000080',
                  '#FDF5E6','#808000','#6B8E23','#FFA500','#FF4500','#DA70D6','#EEE8AA','#98FB98','#AFEEEE','#DB7093','#FFEFD5','#FFDAB9','#CD853F','#FFC0CB','#DDA0DD','#B0E0E6',
                  '#800080','#FF0000','#BC8F8F','#4169E1','#8B4513','#FA8072','#FAA460','#2E8B57', '#FFF5EE','#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#708090','#FFFAFA','#00FF7F',
                  '#4682B4','#D2B48C','#FFFF00','#9ACD32']

        #创建写入
        w = xlwt.Workbook(encoding='utf-8')  # #创建可写的workbook对象,编码改为utf-8
        ws = w.add_sheet('sheet')  # 创建工作表sheet
        hang = 1  # 表示行的意思，在xls文件中写入对应的行数

        #ws.write(0, 0, 'name')  # 0行写入表头
        ws.write(0, 0, 'x_point')  # 0行写入表头
        ws.write(0, 1, 'y_point')  # 0行写入表头
        ws.write(0, 2, 'Cluster')  # 0行写入表头

        #读取用户姓名
        #data = pd.read_excel("D:\\experiment\\第二次\\data\\user_name.xls")  # 如果是csv文件则用read_csv
        # print(data)
        #train_data = np.array(data)  # np.ndarray()每个姓名转换为一个list[]
        # print(train_data)
        #all_list = train_data.tolist()  # 转换list
        #name_list = [i for j in all_list for i in j]  # 去掉一层[]
        index=0

        for i in range(len(x_point)):
            for j in range(len(x_point[i])):
                #ax.annotate(name_list[index], xy=(x_point[i][j], y_point[i][j]), xytext=(x_point[i][j] - 0.5, y_point[i][j]+0.2), fontsize=7)  # 这里xy是需要标记的坐标，xytext是对应的标签坐标
                # 用户按聚类存入
                #ws.write(hang, 0, name_list[index])#存用户名
                ws.write(hang,0,x_point[i][j])#存x轴坐标
                ws.write(hang,1,y_point[i][j])#存y轴坐标
                ws.write(hang,2,i)#存簇数
                hang+=1
                index+=1
                ax.scatter(x_point[i], y_point[i], c=colors[i])
        ax.scatter(x_center_point, y_center_point, marker='*', s=100, c='black')
        w.save("D:\\experiment\\第三次豆瓣\\测试3\\train\\user_Cluster_T1=110,T2=110.xls")
        #w.save("D:\\experiment\\第三次豆瓣\\测试3\\对比实验\\对比实验_K - means聚类结果_K=4.xls")

        plt.title('聚类效果图')
        plt.xlabel("X偏好")
        plt.ylabel("Y偏好")
        plt.show()



