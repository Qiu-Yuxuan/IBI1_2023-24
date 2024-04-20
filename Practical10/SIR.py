import numpy as np#inport necessary library
import matplotlib.pyplot as plt
beta=0.3#set up infectious rate 
gamma=0.05#set up recovery rate
N=10000#set up sample population
susceptible=[]# create a list to store number of susceptible ones
infected=[]#create a list to store number of infected ones
recovered=[]#create a list to store number of recovered ones
current_recovered=0#initialise the number of recovered, infected, susceptible persons
current_infected=1
current_susceptible=9999
for i in range(1000):
    infected_propability=beta*current_infected/N
    new_infected=np.random.choice(range(2),current_susceptible,p=[1-infected_propability,infected_propability])#create a list, 0 means not being infected, 1 means being infected
    count1=0
    for i in new_infected:
        count1+=i#caculate the number of ones be infected newly
    new_recovered=np.random.choice(range(2),current_infected,p=[1-gamma,gamma])#create a list, 0 means not being recovered, 1 means being recovered
    count2=0
    for i in new_recovered:
        count2+=i#caculate the number of ones be recovered newly
    current_infected=count1+current_infected-count2 
    infected.append(current_infected)
    current_recovered=count2+current_recovered
    recovered.append(current_recovered)
    current_susceptible=N-current_recovered-current_infected
    susceptible.append(current_susceptible)
plt.figure(figsize=(8, 6), dpi=150)  
plt.plot(susceptible, label='susceptible')
plt.plot(infected, label='infected')
plt.plot(recovered, label='recovered')
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR Model')
plt.legend()
plt.show()
