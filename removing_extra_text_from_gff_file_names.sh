#! /bin/bash

# Author: Paulina Chilarska

# This script removes a given text string in a file name of all gff files in a given directory. 

# To run: program_path input_file continuous_text_string_to_be_removed

echo ""

echo "Renaming files in the specified directory..."

for f in $1/*.gff; do
	b=`basename $f $2.gff`
	d=`dirname $f`
	mv $f $d/$b.gff
done

echo "Done:)"

echo ""



