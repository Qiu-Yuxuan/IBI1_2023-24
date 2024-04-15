database=open('d:/文档/大一下/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open the file
result=open('d:/文档/大一下/IBI1/IBI1_2023-24/Practical8/duplicate_genes.fa','w')#open the file where I will store the duplicated sequence
import re
description_regex=re.compile(r'^>(\w+)_.+$')#regex that match the description line
whether_duplicate=False #judge whether the part is duplicated part
for line in database:
    description_line=description_regex.match(line)#match the line with the description regex
    if description_line:#if the line is description line
        if 'duplication' in line:
            gene_name=description_line.group(1)#get the gene name
            simplified_sequence=f">{gene_name}\n"
            result.write(simplified_sequence)# write the simplified sequences into output file
            whether_duplicate=True#confirm the line the lines after this line are duplicated part
        else:
            whether_duplicate=False#this is not duplicated part
    else:#this line is sequence
        if whether_duplicate:#if this line is in duplicated part
            result.write(line)#write the dupilated sequence into the output file
database.close()#close the file
result.close()  