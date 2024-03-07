#I need to repeat to double the density and increase the day until the density over 90
# Initialize variables
density=5
day=1
# Loop until the density exceeds 90%
while density<90 :
    density=2*density
    day=day+1
# Output results
print("on the day"+str(day+1),"the cell over 90% density")
print(str(day-1),"is the maxium number of days I can have a holiday stay away from the lab")
