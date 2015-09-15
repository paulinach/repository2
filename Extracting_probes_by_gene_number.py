#!/usr/bin/python

# This program extracts lines from a series matrix (expression data) given a list of Ensembl gene numbers.

# Author: Paulina Chilarska

# First working version saved on: 
# Last working version saved on: 

import sys

# To use: program_path transcript_list annotated_input_series_matrix 'gene list id without spaces + .txt'

# E.g.: /Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/Extracting_probes_by_gene_number.py /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/methylcytosines_h1_all_lines.gff_By_chromosome/75_per_h1_more_no_extension_Ensembl_gene_numbers.txt /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt 75_per_h1_more.txt

OutFileName = sys.argv[2] + '_filtered_by_' + sys.argv[3]

OutFile = open(OutFileName, 'w')

transcript_list_fh = open(sys.argv[1])

enst_list = gene_list_fh.readlines()

transcript_list_fh.close()

fh = open(sys.argv[2])
for line in fh:                            # And then for every next line...
    LineElements = line.split()           # Split your current lineread a list of ENST ids from one file.
    transcript_from_matrix = LineElements[19]
    if transcript_from_matrix in enst_list:
        OutFile.write(line) 

OutFile.close()
fh.close()

print 'Done.'


    
          

