#!/usr/bin/python

# This program counts lines in all gene names' files with the same % cutoff in the file name and adds them together (omitting header lines).

# Author: Paulina Chilarska

# First working version saved on: 15/02/2011
# Last working version saved on: 

import subprocess
import sys

# To use: program_path input_folder_path
# E.g.: /Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/counting_lines_in_gene_files_by_%_cutoff.py  /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/

def wc(file):
     f = open(file)
     cnt = 0
     for line in f:
          cnt = cnt +1
     return cnt

list_of_folder_names = ['methylcytosines_h1_all_lines.gff_By_chromosome/', 'methylcytosines_h1_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_h1_CG-only.gff_By_chromosome/', 'methylcytosines_h1_CHG-only.gff_By_chromosome/', 'methylcytosines_h1_CHH-only.gff_By_chromosome/']
# 'methylcytosines_imr90_all_lines.gff_By_chromosome/', 'methylcytosines_imr90_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_imr90_CG-only.gff_By_chromosome/', '/methylcytosines_imr90_CHG-only.gff_By_chromosome/', 'methylcytosines_imr90_CHH-only.gff_By_chromosome/']



print '\nGoing into loop...\n'







for folder_name in list_of_folder_names:


    out_file = sys.argv[1] + folder_name + '_gene_number.txt'
    fh = open(out_file,"w")
    print out_file
   
    fh.write('# ' + folder_name + '\n')
    fh.write('# %_cutoff        n_genes' + '\n') 
    per_cutoff = 5

   
    for per_cutoff in range(5,100,5):
        cnt = 0

        

   
    
        search_phrase = '_' + str(per_cutoff) + '%_.gff_intersected_with_TSSs.gff_gene_names.txt'
    
        line_count = 0

        for chr_number in range(1,23):

            cnt = cnt + 1

       
            file_path = sys.argv[1] + folder_name + 'chr' + str(chr_number) + '.gff' + '_DDMRs_above' + str(search_phrase)
    
    #       if str(search_phrase) in file_path:        
  
            line_count = line_count + wc(file_path)
          
            print folder_name + '_' + str(chr_number) + '_' + str(per_cutoff) + '_' + str(line_count)
        fh.write(str(per_cutoff) + '            ' + str(line_count) + '\n') 
        
              
 

            
 
  #     folder_path = sys.argv[1] + folder_name  

    fh.close()
                              


     

print '\nDone counting.\n'

print str(cnt) + ' files processed'



