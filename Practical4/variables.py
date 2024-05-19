#training by both running and strength exercises is better
#a = 40
#b = 36
#c = 30
# caculate the difference
#d = a - b
#e = b - c
# compare difference value
#if d > e：
 # output "Training only by running is better."
#if d < e：
  #output"Training by both running and strength exercises is better."
#else：
  #output "Both training are equally good."
a=40
b=36
c=30
d=a-b
e=b-c
if d>e:
  print("Training only by running is better.")
elif d<e:
  print("Training by both running and strength exercises is better.") 
else:
  print("Both training are equally good.") 
X=True
Y=False
W=X!=Y
print("X="+str(X))
print("Y="+str(Y))
print("W="+str(W))
# W is true if X is True and Y is False
#    X       Y         W
#   True    True      False
#   True    False     True
#   False   True      True
#   False   False     False