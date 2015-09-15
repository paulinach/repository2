#!/usr/bin/python

import sys

# This script takes a txt file (e.g. BS-seq data file) with the following order of columns: 

# 1. Chromosome number
# 2. position
# 3. strand (+ or -)
# 4. context (CpG or non-CpG)
# 5. mc (number of methylated cytosines in the reads covering this position)
# 6. reads (number of reads covering this position)
# 7. id (cytosine 'serial' number)

# ...and turns it to gff file with the following order:

# 1. Chromosome number
# 2. Reads
# 3. Context (CpG or non-CpG)
# 4. Start position
# 5. End position (the same as start position)
# 6. mc
# 7. Strand
# 8. Reading frame (not applicable to BS-seq data, just write in a dot)

# To use: program_path input_file output_file


# Open a file to be turned into gff

fileHandle = open ( sys.argv[1] )

# Open or create an output file

OutFile = open(sys.argv[2],"w")

# Give your output file headers in the first line

OutFile.write("Chr\tReads\tContext\tStart\tEnd\tMC\tStrand\tReading_frame \n")
    
# Read the first line of the input file and do nothing

line = fileHandle.readline()    

# Read the second and subsequent lines of the input file in a while loop which splits each line into its elements and prints them into the output file in a new order

line = fileHandle.readline()    

while line:
  
    LineElements = line.split()
  
    OutFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t.\n' % (LineElements[0],LineElements[5],LineElements[3],LineElements[1],LineElements[1],LineElements[4],LineElements[2]))
  
    line = fileHandle.readline()
    
# Close the input file

fileHandle.close()

# Close the output file

OutFile.close()

print "Done :)"

