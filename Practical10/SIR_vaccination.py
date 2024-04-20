import numpy as np
import matplotlib.pyplot as plt
beta=0.3
gamma=0.05
N=10000
vaccinated_rate=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]#creat a list to store vaccinated rate
infected_over_time ={vac: [] for vac in vaccinated_rate}#creat a dictionary whose key is vaccinated rate
for vac in  vaccinated_rate:
    vaccinated=int(vac*(N-1))
    current_recovered=0
    current_infected=1
    current_susceptible=N-vaccinated-current_infected
    susceptible=[]
    infected=[]
    recovered=[]
    for i in range(1000):
        infected_propability=beta*current_infected/N
        new_infected=np.random.choice(range(2),current_susceptible,p=[1-infected_propability,infected_propability])
        count1=0
        for i in new_infected:
            count1+=i
        new_recovered=np.random.choice(range(2),current_infected,p=[1-gamma,gamma])
        count2=0
        for i in new_recovered:
            count2+=i
        current_infected=count1+current_infected-count2 
        current_recovered=count2+current_recovered
        current_susceptible=N-current_recovered-current_infected-vaccinated
        infected_over_time[vac].append(current_infected)
plt.figure(figsize=(8, 6), dpi=150)  
for vaccinated_rate, population in infected_over_time.items():
    plt.plot(range(1000), population, label=f'coverage={vaccinated_rate}')
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR Model')
plt.legend()
plt.show()


