#!/usr/bin/env python

# This program takes three columns from a tab-delimited datafile and does a t-test for their log ratios

# Author: Paulina Chilarska

# First working version saved on: 12/01/11
# Last working version saved on: 

import sys
import math
from scipy import stats
import numpy


# To use: program_path matrix_filtered_by_50_per_imr90_more matrix_filtered_by_50_per_h1_more series_matrix_annotated.txt

# E.g. /Users/paulina/MY_STUFF/PhD_project/Applications/My_scripts/t-test_of_log_ratios.py /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt_filtered_by_50_per_imr90_more.txt /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt_filtered_by_50_per_h1_more.txt /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt

# Create dictionaries of your red and yellow datapoints

yellow_datapoints = {}
red_datapoints = {}

# Write a routine to calculate the means of columns you want and save their log ratios in dictionaries

def datapoint_calculation(file):
    dict = {}
    fh = open(file)           # Open your input file
    fh.readline()
    for line in fh:                            # And then for every next line...
        LineElements = line.split()           # Split your current line
        column_two = LineElements[1]
        column_three = LineElements[2]
        column_four = LineElements[3]
        column_eight = LineElements[7]
        column_nine = LineElements[8]
        column_ten = LineElements[9]
        probe_id = LineElements[0]
        mean_of_columns_two_to_four = numpy.mean([float(column_two), float(column_three), float(column_four)])
        mean_of_columns_eight_to_ten = numpy.mean([float(column_eight), float(column_nine), float(column_ten)])
        means_ratio = mean_of_columns_two_to_four/mean_of_columns_eight_to_ten
        log_means_ratio = math.log10(means_ratio)
	if not probe_id in dict:
            dict[probe_id] = []
        dict[probe_id].append(log_means_ratio)
    return dict.values()

# Run the routine on your columns

yellow_ratios = datapoint_calculation(sys.argv[1])
red_ratios = datapoint_calculation(sys.argv[2])
green_ratios = datapoint_calculation(sys.argv[3])

# green_datapoints = /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt' using (($2 + $3 + $4)/3):(($8 + $9 + $10)/3)

# yellow_datapoints = /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt_filtered_by_50_per_imr90_more.txt' using (($2 + $3 + $4)/3):(($8 + $9 + $10)/3)

# red_datapoints = /Users/paulina/MY_STUFF/PhD_project/ES_cell_differentiation_expression_data/no_quotes_GSE8590_series_matrix_annotated.txt_filtered_by_50_per_h1_more.txt' using (($2 + $3 + $4)/3):(($8 + $9 + $10)/3)

# Run t-test

print '\nt-test of yellow versus red is (t-statistic, p-value):' + str(stats.ttest_ind(yellow_ratios, red_ratios)) + '\n'
print '\nt-test of green versus red is (t-statistic, p-value):' + str(stats.ttest_ind(green_ratios, red_ratios)) + '\n'
print '\nt-test of yellow versus green is (t-statistic, p-value):' + str(stats.ttest_ind(yellow_ratios, green_ratios)) + '\n'
