import csv
import datetime as dt
from datetime import datetime

import matplotlib.pyplot as plt

file_path = "test.csv"

lowests = []
highests = []
dates = []
a=0
with open(file_path, mode='r') as file :
    reader = csv.reader(file)
    header = next(reader)
    for word in reader:
        if word[3]!='':
            date_str = word[2].split("-")[1]
            dates.append(date_str)
            highests.append(float(word[5]))
            lowests.append(float(word[8]))


    print(dates)
    print(highests)
    print(lowests)
#         # print(word[2],float(word[5]),float(word[8]))
#         lowests.append([float(word[5]),float(word[8])])
#         dates.append(word[2])
#         if a==20:
#             break
#         a+=1
#
# plt.plot(dates,lowests)
# plt.show()
###000000
###F98923
plt.bar(dates, lowests, color="#000000", linestyle="-" )
plt.plot(dates, highests, color="#F98923" , marker="o" , linestyle=" ")
plt.title("bleak global warming",fontsize=20)
plt.show()