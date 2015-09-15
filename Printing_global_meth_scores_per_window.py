#!/usr/bin/env python

import sys
import os
import numpy

# Author: Paulina Chilarska

# First working version saved on: 13/01/2011
# Last working version saved on: 

# This script takes a BS-seq results files in gff format and scrutinises them window by window for % methylation. Then prints out the resulting region % methylation values. 

# To use: program_path input_file.gff 
# E.g.: /Users/Paulina/MY_STUFF/PhD_project/Applications/My_scripts/Printing_global_meth_scores_per_window.py /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/methylcytosines_h1_all_non-CpG_lines.gff >/Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/histogram_of_global_methylation_h1_all_non-CpG_lines.txt

# Define a function that returns a dictionary containing region ids as the keys and their methylation level as values

def load_meth_scores(file): 
                                            # This function takes one file at a time 
                    dict = {}               # Create an empty dictionary
                    fh = open(file)           # Open your file whatever it is
                    fh.readline()             # Skip the header line
                    fh.readline()
                    for line in fh:                            # And then for every next line...
                           LineElements = line.split()           # Split your current line
                           position = LineElements[3]
                           score = float(int(LineElements[5]))/int(LineElements[1])    # Calculate the methylation score and round to the nearest integer
                           window_id = int(int(position)/1000)                              # Assign an integer to every window (it changes every 1000 bp)
                           if (not (window_id in dict)):                  # If the window_id is not yet present in your dictionary add it there, creating an empty list
                                 dict[window_id] = []
                           dict[window_id].append(score)                  # Append the current score to the list and go back to the beginning of the loop
                    fh.close()                                            # Close the file handle
                    return dict     # The result of this function is a dictionary of lists of methylation values - now get mean of each list!

# call your function

dict_of_lists = load_meth_scores(sys.argv[1])

# print dict_of_lists

# now get mean of each list!

final_list = []

for window in dict_of_lists:
    list_mean = float(sum(dict_of_lists[window])) / len(dict_of_lists[window])
    final_list.append(list_mean)

# print final_list

# Turn your list into a histogram

hist =  numpy.histogram(final_list, bins=100, range=None, normed=False, weights=None)
histSize = len(hist[0])
for i in range(0, histSize):
    print str(hist[1][i]) + '\t' + str(hist[0][i])



