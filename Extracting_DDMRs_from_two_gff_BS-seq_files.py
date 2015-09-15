#!/usr/bin/python

import sys
import os

# Author: Paulina Chilarska

# First working version saved on: 15/10/2010
# Last working version saved on: 29/10/2010

# This script takes two BS-seq results files in gff format and extracts DDMRs (DNA Differentially 
# Methylated Regions) from them. A DDMR is defined as 1kb window where the % difference between 
# methylation states of all cytosines is = or > e.g. 50%.

# Note: The assumption is that both files contain data for just one chromosome (the same chromosome for both files)

# To use: program_path input_file_1.gff input_file_2.gff
# E.g.: /Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/Extracting_DDMRs_from_two_gff_BS-seq_files.py /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/methylcytosines_h1_all_non-CpG_lines.gff /Users/paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/methylcytosines_imr90_all_non-CpG_lines.gff

# Define a function that returns a dictionary containing region ids as the keys and lists of methylation scores as values

def load_meth_scores(file): 
                                            # This function takes one file at a time 
                    dict = {}               # Create an empty dictionary
                    fh = open(file)           # Open your file whatever it is
                    fh.readline()             # Skip the header line
                    fh.readline()
                    for line in fh:                            # And then for every next line...
                           LineElements = line.split()           # Split your current line
                           position = LineElements[3]
                           chromosome = LineElements[0]
                           context = LineElements[2]
                           score = float(int(LineElements[5]))/int(LineElements[1])    # Calculate the methylation score and round to the nearest integer
                           window_id = int(position)/1000                              # Assign an integer to every window (it changes every 1000 bp)
                           if (not (window_id in dict)):                  # If the window_id is not yet present in your dictionary add it there, creating an empty list
                                 dict[window_id] = []
                           dict[window_id].append(score)                  # Append the current score to the list and go back to the beginning of the loop
                    fh.close()                                            # Close the file handle
                    return dict     # The result of this function is a dictionary of lists

def get_chr(file):                  # This function takes one file at a time             
                    fh = open(file)           # Open your file whatever it is
                    fh.readline()             # Skip the header line
                    line = fh.readline()
                    LineElements = line.split()           # Split your current line
                    chromosome = LineElements[0]        # Get chromosome number from the first line only (this assumes that they are all the same)
                    fh.close()  
                    return chromosome   

def get_context(file):                  # This function takes one file at a time 
                                  
                    fh = open(file)           # Open your file whatever it is
                    fh.readline()             # Skip the header line
                    line = fh.readline()
                    LineElements = line.split()           # Split your current line
                    context = LineElements[2]             # Get chromosome number from the first line only (this assumes that they are all the same)
                    fh.close()  
                    return context    


# First ask your user what cutoff to use:

per_cutoff = raw_input ('Specify the cutoff % difference in the mean methylation scores above which a region will be treated as DDMR:\n')
                                          
# In the body of the script call the function twice to get two dictionaries of regions with their scores

print '...'
print 'Region scores are being calculated...'

file_one_scores = load_meth_scores(sys.argv[1])
file_two_scores = load_meth_scores(sys.argv[2])

# ...and extract chromosome and context from the first line of your first input file

chromosome = get_chr(sys.argv[1])
context = get_context(sys.argv[1])

#  Note: This assumes context and chromosome are the same for all regions in both files!

# In a loop calculate and save as a variable the mean of scores in a given region

print '\nMean scores for every region are being calculated and compared...'

DDMRs = {}

for region in file_one_scores:

    if file_two_scores.get(region):

        file_one_region_mean_score = float(sum(file_one_scores[region])) / len(file_one_scores[region])
        file_two_region_mean_score = float(sum(file_two_scores[region])) / len(file_two_scores[region])

# Calculate and save as a variable the % difference in region means

        region_means_difference = abs((file_one_region_mean_score - file_two_region_mean_score) * 100)

# In a loop, If % difference between mean score of region 0 from H1 is greater than or = to the user-specified % value 
# append to a dictionary called DDMRs wth region id as the key and % difference as the value

        if region_means_difference >= int(per_cutoff):
            DDMRs[region] = region_means_difference

print '\nDDMRs are being saved into a file...'

# In the end print your DDMRs into a new gff

# First open/create a new file

# os.path.dirname(sys.argv[1]) returns directory of the input file, i.e. sys.argv[1]

OutFileName = sys.argv[1] + '_DDMRs_above_' + per_cutoff + '%_' + '.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line. They will be:
# 1. Chromosome where the region starts
# 2. Chromosome where the region ends
# 3. Context (CpG or one of non-CpG contexts)
# 4. Region start position
# 5. Region end position
# 6. % difference in the mean methylation scores between 1kb regions in two input BS-seq data files
# 7. Strand (irrelevant here, just a dot)
# 8. Reading_frame (irrelevant here, just a dot)

OutFile.write("Chr\tSth\tContext\tStart\tEnd\t%_Score_diff\tStrand\tReading_frame \n")

# Open one of your input files

# Then in a loop write in your region coordinates

for DDMR in DDMRs:
  
    OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t.\t.\n' % ( chromosome,'.', context,int(DDMR)+1,int(DDMR)+1001,DDMRs[DDMR]))

# Close the output file

OutFile.close()

print '\nDone.\n'



