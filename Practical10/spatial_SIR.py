import numpy as np #import necessary libraries
import matplotlib.pyplot as plt
population=np.zeros((100,100)) #set up array to store model
beta=0.3#infectious rate
gamma=0.05#recovered rate
outbreak=np.random.choice(range(100),2)#choose the location to outbreak in rondom
population[outbreak[0],outbreak[1]]=1#consider ones infected as 1
for step in range(100):
    plt.figure ( figsize =(6 ,4) , dpi=150)
    plt.imshow ( population , cmap='viridis' , interpolation='nearest')
    plt.title('Step:'+str(step))
    plt.show()#create plot to show every step 
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]#anyone infected can probably be recovered 
plt.figure ( figsize =(6 ,4) , dpi=150)
plt.imshow ( population , cmap='viridis' , interpolation='nearest')
plt.title('Step:'+str(step+1))
plt.show()#show the figure of final step