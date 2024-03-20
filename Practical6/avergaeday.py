average_day={'sleeping':8, 'classes':6, 'studying':3.5, 'TV':2, 'music':1,'other':3.5}#it is the dictionart that record the data
print(average_day)
import matplotlib.pyplot as plt
activity_lablels = ["sleeping", "classes", "studying", "TV", "Music", "other"]#set the abscissa 
time_day =[8, 6, 3.5, 2, 1, 3.5] #set the ordinate
plt.figure()
plt.pie(time_day, labels=activity_lablels, startangle= 90)#set the data and tyle of the figure
plt.title("the average day of a university students")#set the title of the figure
plt.show()#show the figure
plt.clf#close the figure