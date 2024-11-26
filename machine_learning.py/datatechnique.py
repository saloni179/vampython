#the kmean model is a unsupervised machine learning data technique model it Can help you to build k cluster based on data set
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.cluster import KMeans
age = [60,50,40,30,20]
salary = [15000,20000,25000,30000,32000]
# plt.scatter(age,salary,marker = 'o')
# plt.show()
data = list(zip(age,salary))
blank_array = []
for mydata in range(1,6):
    Kmeans = KMeans(n_clusters = mydata)
    Kmeans.fit(data)
    blank_array.append(Kmeans.inertia_)
plt.plot(range(1,6),blank_array,marker = 'o')
plt.show()