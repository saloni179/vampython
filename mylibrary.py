import numpy as np
import pandas as pd

#create an array start from 0 to 49
arr = np.arange(10000)
1 * 50
50 * 1
2 * 25
25 * 2
5 * 10
10 * 5

#find the min,nax,mean from arr
print("mean is",arr.mean())
print("max is",arr.max())
print("min is",arr.min())
mydata = arr.reshape(100,100)
print("mydata shape is",mydata.shape)
print(mydata)
print("shape is",arr.shape)
print(arr)
# array slicing
print(arr[:])
#[0,1,2,3,4,5,6,7,8,9]
emp=np.array([5,6,3,2,1,9,10,4,7,8])
print(emp[:-5])

#pandas will represent the dataset in dataframes
myDataFrame= pd.DataFrame()
myDataFrame=pd.DataFrame(data=np.arange(0,50).reshape(5,10))
print(myDataFrame)
print("mean",myDataFrame.mean())
print("median",myDataFrame.median())
print("mode",myDataFrame.mode())
print(myDataFrame.head(1))
print(myDataFrame.tail())
print(myDataFrame.loc[[6,]])