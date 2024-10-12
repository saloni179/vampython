import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2020,2021,2022,2023])
grades = np.array([85,80,79,73])

#show data in graph- line   (x,y),pie(x)
#bar(x,y),scatters(x,y)
# plt.plot(years,grades,marker = 'o')
# #give the graph title
# plt.title("academic growth")
# #set the name for x and y axis
# plt.xlabel("passing years")
# plt.ylabel("students marks")
# plt.show()
#Note in line,bar,scatters graph the dataset must be same size

trendingLangName = np.array(['python','javascript','java','c'])
trendingLang = np.array([45,30,20,5])
plt.title("trending language marketplace")

# plt.pie(trendingLang)
# plt.legend(trendingLangName)
# plt.show()

#jio 5 years sell growth, 2020 -2024
sales = np.array(['200','250','300','280','320'])
salesyears = np.array(['2020','2021','2022','2023','2024'])
plt.bar(sales,salesyears)
plt.grid()
plt.show()