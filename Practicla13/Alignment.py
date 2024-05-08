import blosum as bl 
with open('d:/文档/大一下/IBI1/IBI1_2023-24/Practicla13/SLC6A4_HUMAN.fa') as SLC6A4_HUMAN:
    seq_human=''
    for line in SLC6A4_HUMAN:
        line=line.replace('\n','')
        if not line.startswith('>'):
            seq_human+=line
with open('d:/文档/大一下/IBI1/IBI1_2023-24/Practicla13/SLC6A4_MOUSE.fa') as SLC6A4_MOUSE:
    seq_mouse=''
    for line in SLC6A4_MOUSE:
        line=line.replace('\n','')
        if not line.startswith('>'):
            seq_mouse+=line
with open('d:/文档/大一下/IBI1/IBI1_2023-24/Practicla13/SLC6A4_RAT.fa') as SLC6A4_RAT:
    seq_rat=''
    for line in SLC6A4_RAT:
        line=line.replace('\n','')
        if not line.startswith('>'):
            seq_rat+=line
matrix= bl.BLOSUM(62)         # Use BLOSUM62 to obtain the scores
alignment_score1=0
for i in range(len(seq_human)):
    animo1=seq_human[i]
    animo2=seq_mouse[i]
    alignment_score1+=matrix[animo1][animo2]
print('Alignment score between human and mouse is',alignment_score1)
alignment_score2=0
for i in range(len(seq_human)):
    animo1=seq_human[i]
    animo2=seq_rat[i]
    alignment_score2+=matrix[animo1][animo2]
print('Alignment score between human and rat is',alignment_score2)
alignment_score3=0
for i in range(len(seq_mouse)):
    animo1=seq_mouse[i]
    animo2=seq_rat[i]
    alignment_score3+=matrix[animo1][animo2]
print('Alignment score between rat and mouse is',alignment_score3)
edit_distance1=0
for i in range(len(seq_human)):
    if seq_human[i]!=seq_mouse[i]:
        edit_distance1+=1
identical_percentage1=(len(seq_human)-edit_distance1)/len(seq_human)*100
print('The identical percentage between human and mouse is',identical_percentage1,'%')
edit_distance2=0
for i in range(len(seq_human)):
    if seq_human[i]!=seq_rat[i]:
        edit_distance2+=1
identical_percentage2=(len(seq_human)-edit_distance2)/len(seq_human)*100
print('The identical percentage between human and rat is',identical_percentage2,'%')
edit_distance3=0
for i in range(len(seq_mouse)):
    if seq_rat[i]!=seq_mouse[i]:
        edit_distance3+=1
identical_percentage3=(len(seq_human)-edit_distance3)/len(seq_mouse)*100
print('The identical percentage between rat and mouse is',identical_percentage3,'%')

    
    
		
		
