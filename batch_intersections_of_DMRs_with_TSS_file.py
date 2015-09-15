#!/usr/bin/python

# This program takes a number of DMR files from a given folder and intersects them with a TSS file..

# Author: Paulina Chilarska

# First working version saved on: 10/02/2011
# Last working version saved on: 14/02/2011

import subprocess
import os
import sys

# To use: program_path input_folder_path
# E.g.: /Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/batch_intersections_of_DMRs_with_TSS_file.py  /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/

# list_of_folder_names = ['methylcytosines_h1_all_lines.gff_By_chromosome/', 'methylcytosines_h1_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_h1_CG-only.gff_By_chromosome/', 'methylcytosines_h1_CHG-only.gff_By_chromosome/', 'methylcytosines_h1_CHH-only.gff_By_chromosome/']
# 'methylcytosines_imr90_all_lines.gff_By_chromosome/', 'methylcytosines_imr90_all_non-CpG_lines.gff_By_chromosome/', 'methylcytosines_imr90_CG-only.gff_By_chromosome/', '/methylcytosines_imr90_CHG-only.gff_By_chromosome/', 'methylcytosines_imr90_CHH-only.gff_By_chromosome/']

def TSS_intersection(file):
    outfile = file + "_intersected_with_TSSs.gff"
    out_file_handle = open(outfile, 'w');
    p = subprocess.Popen(['java', 'gfftools.RetainOverlapping', file, '/Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/ncbi36-tss.gff'],
    stdout=out_file_handle, shell=False)
    p.wait()
    out_file_handle.close()
    return None



print '\nGoing into loop...\n'


cnt = 0
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
                if file_name.find('DDMRs') >= 0:
                    TSS_intersection(path_name)


print "\nDone.\n"
