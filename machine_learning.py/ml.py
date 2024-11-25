import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt
#mean -> avg value
#median -> middle value when arranged
#mode -> most repeated value 
# salary = [65000,85000,90000,70000,80000, 65000]
# print(np.mean(salary)) #mean
# print(np.max(salary))
# print(np.min(salary))
# print(np.median(salary)) #median
# print(st.mode(salary)) #mode
# print(np.std(salary)) #standard deviation
# print(np.var(salary)) #variance
data = (np.random.randint(0,10,100))
print(data)
plt.hist(data)
plt.show()
#normal and uniform data
plt.uniform(data)