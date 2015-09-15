#!/usr/bin/python

import sys

# Open a file to be turned into CG-only gff

fileHandle = open ( sys.argv[1] )

# Create an output file

OutFileName = sys.argv[1] + '_CG-only.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop checking if they contain CG
# If yes, split line into its elements and prints them into the output file in a new order
# If not look at another line

line = fileHandle.readline()    

if 'CG' in line:

    while line:
  
        LineElements = line.split()
  
        OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2]))
  
        line = fileHandle.readline()
        
else:
  
    line = fileHandle.readline()
    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "CG-only gff created."
