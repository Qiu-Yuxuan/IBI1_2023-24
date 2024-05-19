average_day={'sleeping':8, 'classes':6, 'studying':3.5, 'TV':2, 'music':1}#it is the dictionart that record the data
other_hours=24-average_day['sleeping']-average_day['classes']-average_day['studying']-average_day['TV']-average_day['music']
average_day['other']=other_hours
print(average_day)
import matplotlib.pyplot as plt
activity_lablels = ["sleeping", "classes", "studying", "TV", "Music", "other"]#set the abscissa 
time_day =[average_day['sleeping'],average_day['classes'],average_day['studying'],average_day['TV'],average_day['music'],average_day['other']] #set the ordinate
plt.figure()
plt.pie(time_day, labels=activity_lablels, startangle= 90)#set the data and tyle of the figure
plt.title("the average day of a university students")#set the title of the figure
plt.show()#show the figure
plt.clf()#close the figure