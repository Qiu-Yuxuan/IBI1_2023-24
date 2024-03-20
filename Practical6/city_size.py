uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
print(uk_cities)
print(china_cities)
import numpy as np
import matplotlib.pyplot as plt
uk_cityname=["Edinburgh","Glasgow","Stirling","London"]
uk_populations=uk_cities
width=0.5
plt.figure()
plt.bar(uk_cityname,uk_populations,width)
plt.ylabel("populations")
plt.title("populations of uk cities")
plt.show()
china_cityname=["Haining","Hangzhou","Shanghai","Beijing"]
china_populations=china_cities
plt.figure()
plt.bar(china_cityname,china_populations,width)
plt.ylabel("populations")
plt.title("populations of china cities")
plt.show()
plt.clf
