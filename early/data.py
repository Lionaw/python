#Lionaw
import pandas as pd
import random

#列表
a = [1,2,3]
b = random.sample(range(0,10),3)

dataframe = pd.DataFrame({'a':a,'b':b})

dataframe.to_csv("test.csv",index=False,sep=',')