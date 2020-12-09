
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#解决matplottlib显示中文的问题
# 仅适用于Windows
plt.rcParams['font.sans-serif']=['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus']=False  #解决保存图像时符号-显示为方块的2问题
'''
对比分析：
绝对数对比（相减）
相对数对比（相除）
结构分析
比例分析
空间分析比较
动态对比分析
'''
data = pd.DataFrame(np.random.rand(30,2)*1000,
                  columns = ['A_sale','B_sale'],
                  index = pd.period_range('20170601','20170630'))
print(data.head())
# 创建数据 → 30天内A/B产品的日销售额

data.plot(kind='line',
      style = '--.',
      alpha = 0.8,
      figsize = (10,3),
      title = 'AB产品销量对比-折线图',
      rot=20)
# 折线图比较

data.plot(kind = 'bar',
      width = 0.8,
      alpha = 0.8,
      figsize = (10,3),
      title = 'AB产品销量对比-柱状图')
# 多系列柱状图比较
plt.show()

# =================================1、绝对数比较 → 相减=============
# （3）柱状图堆叠图+差值折线图比较
fig3 = plt.figure(figsize=(10,6))
plt.subplots_adjust(hspace=0.3)
# 创建子图及间隔设置
ax1 = fig3.add_subplot(2,1,1)
x = range(len(data))
y1 = data['A_sale']
y2 = -data['B_sale']
plt.bar(x,y1,width = 1,facecolor = 'yellowgreen')
plt.bar(x,y2,width = 1,facecolor = 'lightskyblue')
plt.title('AB产品销量对比-堆叠图')
plt.grid()
plt.xticks(range(0,30,6))
ax1.set_xticklabels(data.index[::6])   #x轴的坐标标签
# 创建堆叠图

ax2 = fig3.add_subplot(2,1,2)
y3 = data['A_sale']-data['B_sale']
plt.plot(x,y3,'--go')
plt.axhline(0,hold=None,color='r',linestyle="--",alpha=0.8)  # 添加y轴参考线
plt.grid()
plt.title('AB产品销量对比-差值折线')
plt.xticks(range(0,30,3))               #个数 这里是三个是一个间隔  共10个  和下面的一样
ax2.set_xticklabels(data.index[::3])    #显示日期  否则就是显示整数 以三天为一个间隔
# 创建差值折线图
plt.show()
