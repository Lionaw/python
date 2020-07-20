import csv
from matplotlib import pyplot as plt 
from datetime import datetime
filename = "death_valley_2014.csv" #配置目录下的文件

with open(filename) as f:
    reader = csv.reader(f)
    header_rows = next(reader)
    
    dates,highs,lows= [],[],[]
    for row in reader:        #遍历除第一行的所有行
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")  #将字符串转化为日期
            high = int(row[1])    #将字符串转化为数字
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)    #将第二列元素添加到high列表
            lows.append(low)


#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='green',alpha=0.5)     #alpha 指定颜色的透明度
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='red',alpha=0.1)   #fill_between() 接受一个x值以及其对应的两个Y值，并填充颜色，facecolor填充颜色

title="Daily high and low temperatures —— 2014\nDeath valley,CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',direction='out',labelsize=16)

plt.show()