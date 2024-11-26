import matplotlib.pyplot as plt
from scipy import stats as st
from sklearn.metrics import r2_score
import numpy as np
age = [20,25,45,30,50,40]
salary = [20000,75000,15000,85000,60000,25000]

# plt.scatter(age,salary)
# plt.show()
# slope,intercept,r,p,std_crr =st.linregress(age,salary)
# print("slope",slope,"intercept",intercept,"r",r,"p",p,"std_crr",std_crr)


#not -> if r is near to 1 -> best case
#if r is near to 0 -> bad case
# def futuresalary(age):
#  return slope*age + intercept
# print(futuresalary(35))
# note -> when we apply linear regression
futuredata = np.poly1d(np.polyfit(age,salary,3))
print(r2_score,salary,futuredata(35))

