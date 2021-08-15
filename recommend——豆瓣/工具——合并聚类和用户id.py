import pandas as pd
import numpy as np
import xlwt

file1="D:\\experiment\\第三次豆瓣\\测试3\\train\\user_id_xy.xls"
file2="D:\\experiment\\第三次豆瓣\\测试3\\train\\user_Cluster_T1=110,T2=110.xls"
outfile="D:\\experiment\\第三次豆瓣\\测试3\\train\\user_id_Cluster_T1=110,T2=110.xls"
data1=pd.read_excel(file1)
train_data1 = np.array(data1)#np.ndarray()每个姓名转换为一个list[]
#print(train_data)
all_list1=train_data1.tolist()#转换list
print(all_list1)
data2=pd.read_excel(file2)
train_data2 = np.array(data2)#np.ndarray()每个姓名转换为一个list[]
#print(train_data)
all_list2=train_data2.tolist()#转换list
print(all_list2)

#创建写入
w = xlwt.Workbook(encoding='utf-8')  # #创建可写的workbook对象,编码改为utf-8
ws = w.add_sheet('sheet')  # 创建工作表sheet
index = 1  # 表示行的意思，在xls文件中写入对应的行数
ws.write(0, 0, 'userid')  # 0行写入表头
ws.write(0, 1, 'cluster')  # 0行写入表头
ws.write(0, 2, 'x')
ws.write(0, 3, 'y')

for item in all_list1:
    user_id=item[0]
    #print(item[1]," ",item[2])
    for itemj in all_list2:
        cluster_num=itemj[2]
        if abs(item[1] - itemj[0]) < 0.00000001 and abs(item[2] - itemj[1]) < 0.00000001:
            ws.write(index, 0, user_id)
            ws.write(index, 1, cluster_num)
            ws.write(index, 2, item[1])#x
            ws.write(index, 3, item[2])#y
            index+=1
            break
w.save(outfile)