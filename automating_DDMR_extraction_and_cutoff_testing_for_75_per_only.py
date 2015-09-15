#!/usr/bin/python

import subprocess
import sys

# This script runs the DDMR extracting script on structured data folder testing various % cutoff values

# Author: Paulina Chilarska

# First working version saved on: 16/11/2010
# Last working version saved on: 08/12/2010

#  To use: program_path input_folder
# E.g.: /Users/Paulina/MY_STUFF/PhD_project/Applications/My_scripts/automating_DDMR_extraction_and_cutoff_testing_for_75_per_only.py /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/methylcytosines_h1_all_non-CpG_lines.gff_By_chromosome/

# Set list item number to 0

x = 0

# Take the y'th gff from h1 folder (initially set to 1)

y = 1

list_of_h1_data_types = ['/methylcytosines_h1_all_lines.gff_By_chromosome/', '/methylcytosines_h1_all_non-CpG_lines.gff_By_chromosome/', '/methylcytosines_h1_CG-only.gff_By_chromosome/', '/methylcytosines_h1_CHG-only.gff_By_chromosome/', '/methylcytosines_h1_CHH-only.gff_By_chromosome/']

list_of_imr90_data_types = ['/methylcytosines_imr90_all_lines.gff_By_chromosome/', '/methylcytosines_imr90_all_non-CpG_lines.gff_By_chromosome/', '/methylcytosines_imr90_CG-only.gff_By_chromosome/', '/methylcytosines_imr90_CHG-only.gff_By_chromosome/', '/methylcytosines_imr90_CHH-only.gff_By_chromosome/']

print 'Looping...'

for item in list_of_imr90_data_types:

    import time

    hour = time.localtime()[3]
    if hour < 12:
        print 'Good morning'
    else:
        print 'Good afternoon'


# Run DDMR-finding
# script 19 times, increasing % cutoff from 5% to 95% by 5% increments. 

# Set z to 5 and increment by 5 every iteration (this is your cutoff testing)

   
    y = 1
    while y < 24:
        print 'How are you?'
    
        z = 30
       

        h1_file_path = sys.argv[1] + list_of_h1_data_types[x] + 'chr' + str(y) + '.gff'

        imr90_file_path = sys.argv[1] + list_of_imr90_data_types[x] + 'chr' + str(y) + '.gff'
        print 'Very well, thank you.'
        p = subprocess.Popen(['/Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/Extracting_DDMRs_from_two_gff_BS-seq_files_without_user_input.py', str(h1_file_path), str(imr90_file_path), str(z)], shell=False)
        p.wait()
            

        y = y + 1
    x = x + 1

#  The procedure skips chromosomes x and y

print 'Done EVERYTHING.'

