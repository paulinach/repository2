#!/usr/bin/python

import sys

# Author: Paulina Chilarska

# Working version saved on: 14/10/2010

# This script takes a txt file (e.g. BS-seq data file) with the following order of columns: 

# 1. Chromosome number
# 2. position
# 3. strand (+ or -)
# 4. context (CpG or non-CpG)
# 5. mc (number of methylated cytosines in the reads covering this position)
# 6. reads (number of reads covering this position)
# 7. id (cytosine 'serial' number)

# ...and turns it to five gff files sorting by context (everything together, CG, CHH, CHG, both non-CpG together).
# All gff files have the following order of columns:

# 1. Chromosome number
# 2. Reads
# 3. Context (CpG or non-CpG)
# 4. Start position
# 5. End position (the same as start position)
# 6. mc
# 7. Strand
# 8. Reading frame (not applicable to BS-seq data, just write in a dot)

# To use: program_path input_file

# Open a file to be turned into general gff

fileHandle = open ( sys.argv[1] )

# Create an output file

OutFileName = sys.argv[1] + '_all_lines.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop which splits each line into its elements and prints them into the output file in a new order

print '\nLooping...\n'

line = fileHandle.readline()    

while line:
  
    LineElements = line.split()
  
    OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2]))
  
    line = fileHandle.readline()
    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "General gff created.\n"

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

print 'Looping...\n'

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

print "CG-only gff created.\n"

# Open a file to be turned into CHG-only gff

fileHandle = open ( sys.argv[1] )

# Create an output file

OutFileName = sys.argv[1] + '_CHG-only.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop checking if they contain CHG
# If yes, split line into its elements and prints them into the output file in a new order
# If not look at another line

print 'Looping...\n'

line = fileHandle.readline()    

while line:    

    if (line.find('CHG') != -1):
        
    	LineElements = line.split()

    	OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2])) 	
	
    line = fileHandle.readline()
	    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "CHG-only gff created.\n"

# Open a file to be turned into CHH-only gff

fileHandle = open ( sys.argv[1] )

# Create an output file

OutFileName = sys.argv[1] + '_CHH-only.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop checking if they contain CHH
# If yes, split line into its elements and prints them into the output file in a new order
# If not look at another line

print 'Looping...\n'

line = fileHandle.readline()    

while line:

    if (line.find('CHH') != -1):

        LineElements = line.split()
    
        OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2]))

    line = fileHandle.readline()
    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "CHH-only gff created.\n"

# Open a file to be turned into all_non-CpG_lines gff

fileHandle = open ( sys.argv[1] )

# Create an output file

OutFileName = sys.argv[1] + '_all_non-CpG_lines.gff'

OutFile = open(OutFileName, 'w')

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop checking if they contain CH
# If yes, split line into its elements and prints them into the output file in a new order
# If not look at another line

print 'Looping...\n'

line = fileHandle.readline()    

while line:

    if (line.find('CH') != -1):

        LineElements = line.split()
    
        OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2]))

    line = fileHandle.readline()
    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "all_non-CpG_lines gff created.\n"

print 'Done :)\n\n'

