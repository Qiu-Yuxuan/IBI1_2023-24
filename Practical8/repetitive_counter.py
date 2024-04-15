seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
element1='GTGTGT'
element2='GTCTGT'
start=0
count1=0
while True:
    start1=seq.find(element1,start)
    if start1==-1:
        break
    else:
        count1+=1
        start=start1+1
start=0
count2=0
while True:
    start1=seq.find(element2,start)
    if start1==-1:
        break
    else:
        count2+=1
        start=start1+1
total_number=count1+count2
print("total number is",total_number)




