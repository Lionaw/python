#Lionaw
import csv
x = input()
a=[]
while x not in 'abc':
    a.append(x)
    x = input()
print(a)
with open("统计.csv",'w',newline='') as t:#numline是来控制空的行数的
    writer=csv.writer(t)#这一步是创建一个csv的写入器
    writer.writerows(a)