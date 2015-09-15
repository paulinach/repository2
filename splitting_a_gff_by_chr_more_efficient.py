#!/usr/bin/python

import sys
import os

# This script splits a gff file by chromosome. The result is many files on chromosome data per file.

# Author: Paulina Chilarska

# Last working version saved on: 03/11/2010

# To use: program_path input_file.gff

# Here is the splitting function:

def split_by_chr(file):
    """Splits gff file by chromosome name and saves in a dictionary where the chr is a key and the lines are values"""
    chr_to_file = {}
    fh = open(file)           # Open your file whatever it is
    fh.readline()      
    for line in fh:
            dirname = os.path.basename(sys.argv[1]) + '_By_chromosome'
            if not os.path.isdir(os.path.dirname(sys.argv[1]) + '/' + dirname + '/'):                      # if By_chromosome directory doesn't exist...
                os.mkdir(os.path.dirname(sys.argv[1]) + '/' + dirname + '/')            # ...make it!
            LineElements = line.split()           # Split your current line
            chromosome = LineElements[0]
            if chromosome not in chr_to_file:
                  OutFile = os.path.dirname(sys.argv[1]) + '/' + dirname + '/' + 'chr' + chromosome + '.gff'
                  chr_to_file[chromosome] = open(OutFile, 'w')
                  chr_to_file[chromosome].write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame\n")
            chr_to_file[chromosome].write(line)

    for chromosome in chr_to_file:
           chr_to_file[chromosome].close()
    return None

    
# Call the function

print '\nSplitting...'

split_by_chr(sys.argv[1])

print '\nDone.\n'


# def split_by_chr(file):
  #   """Splits gff file by chromosome name and saves in a dictionary where the chr is a key and the lines are values"""
  #   chrFiles = {}
  #   fh = open(file)           # Open your file whatever it is
  #   fh.readline()             # Skip the header line
   #  lines_loaded = fh.readlines()
   #  for line in lines_loaded:
   #   #   if line.strip():              # Skip empty lines
   #   #       continue
   #          LineElements = line.split()           # Split your current line
   #          chromosome = LineElements[0]
   #          if (chromosome not in chrFiles):
   #              chrFiles[chromosome] = [] 
   #          chrFiles[chromosome].append(line)
   #          
   #  fh.close()   
   #  return chrFiles

"""

def save_dict(dict):
 #   Saves a dictionary as a series of gff files where keys are file names and values are lines.
    dirname = os.path.basename(sys.argv[1]) + '_By_chromosome'
    if not os.path.isdir(os.path.dirname(sys.argv[1]) + '/' + dirname + '/'):                      # if By_chromosome directory doesn't exist...
            os.mkdir(os.path.dirname(sys.argv[1]) + '/' + dirname + '/')            # ...make it!
    for chromosome in dict:
        OutFile = os.path.dirname(sys.argv[1]) + '/' + dirname + '/' + 'chr' + chromosome + '.gff'
        fh = open(OutFile, 'w')
        fh.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame\n") 
        for key in dict:
                for line in dict[key]:
                   if line.startswith(chromosome):
                       print >> fh, line + '\n' 
        fh.close()
    return None

       

# Call your function to split a file

print '\nSplitting the input file...\n'

dict_of_chromosomes = split_by_chr(sys.argv[1])

# Call your saving function to save new files

print 'Saving new files by chromosome...\n'

save_dict(dict_of_chromosomes)

print 'Done.\n'

"""

