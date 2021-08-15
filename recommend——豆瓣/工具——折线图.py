# encoding=utf-8
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']#支持中文
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


names = ['5', '10', '15', '20', '25']
x = range(len(names))
y = [3.88, 7.3, 10.27, 12.91, 15.2]#本文算法，准确率/召回率
y1=[3.85, 6.63, 9.68, 12.47, 14.92]#单独K-means，准确率/召回率


#plt.figure(dpi=150, figsize=(10,5))#画布大小
plt.axis([0, 3, 3, 16])#设定x轴y轴范围
plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'本文平均召回率')
plt.plot(x, y1, marker='*', ms=10,label=u'对比实验平均召回率')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45, fontsize=25)
plt.yticks(fontsize=25)
plt.margins(0)
plt.subplots_adjust(bottom=0.1)
plt.xlabel(u"Top-N推荐N值", fontsize=25) #X轴标签
plt.ylabel("推荐平均召回率", fontsize=25) #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

#plt.savefig('本文算法平均准确率和召回率', dpi=300)
