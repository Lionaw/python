import re

madFile = open('.\py814\chapter8\mad.txt')
mad1con = madFile.read()
print(mad1con)

#正则
mad1Regex = re.compile(r'adjective',re.I)
n1=input("Enter an adjective:\n")
mad2con = mad1Regex.sub(n1,mad1con)
mad2Regex = re.compile(r'noun',re.I)
n2=input("Enter an noun:\n")
mad3con = mad2Regex.sub(n2,mad2con,1)
mad3Regex = re.compile(r'verb',re.I)
n3=input("Enter an verb:\n")
mad4con = mad3Regex.sub(n3,mad3con)
mad4Regex = re.compile(r'noun',re.I)
n4=input("Enter an noun:\n")
mad2con = mad4Regex.sub(n4,mad4con,2)

mad2File = open('.\py814\chapter8\mad1.txt','w')
mad2File.write(mad2con)
madFile.close()
mad2File.close()