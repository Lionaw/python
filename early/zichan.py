#Lionaw
import pandas as pd
import csv

print("资产类型：\n\ta1,a2,a3\n\tb1,b2,b3")
a=[]
b=[]
c=[]
d=[]
i=0
ty_1 = input("请输入资产类型：")
while ty_1 != 'exit()':
    if ty_1 in 'a1a2a3b1b2b3':
        a.append(ty_1)
        b.append(input("请输入资产金额："))
        c.append(input("请输入发生时间："))
        d.append(input("备注"))
        ty_1 = input("请输入资产类型：")
        i=i+1
    else:
         break



with open("资产.csv",'w',newline='') as f:
    head = ['a','b','c','d']
    rows = [{'a':a[1],'b':b[1],'c':c[1],'d':d[1]}]
    writer = csv.DictWriter(f,head)
    writer.writeheader()
    writer.writerows(rows)