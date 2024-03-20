average_day={'sleeping':8, 'classes':6, 'studying':3.5, 'TV':2, 'music':1,'other':3.5}
print(average_day)
import matplotlib.pyplot as plt
activity_lablels = ["sleeping", "classes", "studying", "TV", "Music", "other"]
time_day =[8, 6, 3.5, 2, 1, 3.5]
plt.figure()
plt.pie(time_day, labels=activity_lablels, startangle= 90)
plt.show()
plt.clf