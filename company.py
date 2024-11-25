#top10 employee fired in 10 million employees
import numpy as np
import pandas as pd
import json
#create 1 million employees using numpy
emp = np.arange(0,1000000)
#fired top10 highest paid employees
highest = pd.DataFrame(data = emp.reshape(100000,10))
print(highest.head(1)+500)

#Average 100000 employees provide bonus of 100 for their increment
myDataFrame = pd.DataFrame(data=np.arange(0,1000000).reshape(100000,10))
print(myDataFrame)
print(myDataFrame.loc[[45000,55000]]+100)

mydata = np.arange(0,12)
DataFrame = pd.DataFrame(data = mydata.reshape(3,4))
print(DataFrame)
print(DataFrame.iloc[1:3,1:3])

DataFrame.to_json("sample.json")
DataFrame.to_csv("sample.csv")
DataFrame.to_excel("sample.xlsx")