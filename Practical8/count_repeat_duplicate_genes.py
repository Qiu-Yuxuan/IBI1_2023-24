import re
repeat_seq = input("'GTGTGT' or 'GTCTGT': ") #input the repeat sequence
input_file='d:/文档/大一下/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_filename = f"{repeat_seq}_duplicate_genes.fa"        #use repeat sequence as file name
output_dir = 'd:/文档/大一下/IBI1/IBI1_2023-24/Practical8/'
output_file = output_dir + output_filename
with open(input_file) as original_file, open(output_file,'w') as result: #open input_file and creat and open output_file meanwhile
    gene_name = None     #initialize the name of the current gene
    gene_sequence = ""        # Initialize the current gene sequence
    for line in original_file:
        if line.startswith(">"): #judge whether this line is gene description
            if gene_name and gene_sequence:   # if the gene name and gene seqence has been stored
                count = gene_sequence.count(repeat_seq)      # count the number of duplicated element
                result.write(f">{gene_name} \n")    # write the gene name on the first line
                result.write(f"{count}  {gene_sequence} \n")  # write the duplicated times and  DNA sequence
            gene_name = line.rstrip()[1:].split('_')[0]     # store or refresh the new gene name
            gene_sequence = "" #initialize the gene sequence again
        else:
            gene_sequence += line.rstrip()        # store the sequence into vairble line by line