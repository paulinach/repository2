#! /bin/bash

# Author: Paulina Chilarska

# In general to add "chr" in front of chromosome number in a gff file run the following command:

# cat file-without-chr.gff | awk '{print "chr" $0}' >file-with-chr.gff

# This script does it for you.

# To run: program_path input_file

echo ""

echo "Adding 'chr'..."

b=`basename $1 .gff`
d=`dirname $1`

cat $1 | awk '{print "chr" $0}' >$d/$b.with_chr.gff

echo "Done :)"

echo ""

