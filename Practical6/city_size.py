uk_cities=[0.56,0.62,0.04,9.7]#store the population sizes
china_cities=[0.58,8.4,29.9,22.2]#store the population sizes
uk_cities.sort()
china_cities.sort()
print(uk_cities)
print(china_cities)
import matplotlib.pyplot as plt
uk_cityname=["Edinburgh","Glasgow","Stirling","London"]#set the abscissa
uk_populations=uk_cities#set the ordinate
width=0.5#set the width
plt.figure()
plt.bar(uk_cityname,uk_populations,width)
plt.ylabel("populations")#set the y axis label
plt.title("populations of uk cities")#set the title
plt.show()#show the figure
china_cityname=["Haining","Hangzhou","Shanghai","Beijing"]#set the abscissa
china_populations=china_cities#set the ordinate
plt.figure()
plt.bar(china_cityname,china_populations,width)#set the style and data
plt.ylabel("populations")#set the y axis label
plt.title("populations of china cities") #set the title
plt.show()#show the figure
plt.clf()#close the figure
