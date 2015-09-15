#!/usr/bin/python

# This program takes a number of DMR files intersected with a TSS file and extracts genes from them.

# Author: Paulina Chilarska

# First working version saved on: 
# Last working version saved on: 

import subprocess
import os
import sys

# To use: program_path input_folder_path
# E.g.: /Users/Paulina/MY_STUFF/PhD_project/Applications/My_scripts/batch_gene_extractions_from_TSS-intersected_files.py  /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/

# list_of_folder_names = ['methylcytosines_h1_all_lines.gff_By_chromosome/', 'methylcytosines_h1_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_h1_CG-only.gff_By_chromosome/', 'methylcytosines_h1_CHG-only.gff_By_chromosome/', 'methylcytosines_h1_CHH-only.gff_By_chromosome/']
# 'methylcytosines_imr90_all_lines.gff_By_chromosome/', 'methylcytosines_imr90_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_imr90_CG-only.gff_By_chromosome/', '/methylcytosines_imr90_CHG-only.gff_By_chromosome/', 'methylcytosines_imr90_CHH-only.gff_By_chromosome/']

def extract_genes(file):
    outfile = file + "_gene_names.txt"
    out_file_handle = open(outfile, 'w');
    p = subprocess.Popen(['java gfftools.GFFMine -attribute ensembl.gene_id ' + file + ' | sort | uniq'], stdout=out_file_handle, shell=True)
    p.wait()
    out_file_handle.close()
    return None



print '\nGoing into loop...\n'


list_of_folder_names = os.listdir(sys.argv[1])

for folder_name in list_of_folder_names:
    if os.path.basename(folder_name).startswith('.'):
        continue
    current_directory = sys.argv[1] + folder_name
    d = sys.argv[1] + '/' + folder_name
    if os.path.isdir(d):
        for file_name in os.listdir(d):
            path_name = d + '/' + file_name
            if os.path.isfile(path_name):
                if file_name.find('intersected_with_TSSs') >= 0:
                    extract_genes(path_name)
                    print '\nGenes extracted from ' + file_name + '\n'


print "\nDone.\n"




