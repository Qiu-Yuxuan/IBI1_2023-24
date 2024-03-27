import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("d:/文档/大一下/IBI1/IBI1_2023-24/Practical7")
dalys_data=pd.read_csv("dalys-rate-from-all-causes(1).csv")
print(dalys_data.head(5))
dalys_data.info()
print(dalys_data.describe())
my_columns=[True,True,False,True]
print(dalys_data.iloc[0:3,my_columns])
print(dalys_data.loc[dalys_data['Entity'] == "Afghanistan","DALYs"])
china_data=dalys_data.loc[dalys_data['Entity']=="China",["Entity","Year","DALYs"]]
china_mean=china_data["DALYs"].mean()
china_DALYs_in_2019=int(china_data.loc[china_data['Year']==2019,"DALYs"])
print(china_mean>china_DALYs_in_2019)
plt.plot(china_data.Year, china_data.DALYs,'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.title('DALYs in China these years')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.show()
UK_DALYs=dalys_data.loc[dalys_data['Entity']=="United Kingdom","DALYs"]
china_DALYs=dalys_data.loc[dalys_data['Entity']=="China","DALYs"]
year=dalys_data.loc[dalys_data['Entity']=="United Kingdom","Year"]
plt.plot(year,UK_DALYs,marker='o',linestyle='-',color='b',label='UK')
plt.plot(year,china_DALYs,marker='s',linestyle='--',color='r',label='China')
plt.title('DALYs in UK and China these years')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.legend()
plt.show()