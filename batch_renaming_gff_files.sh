#! /bin/bash

# This script renames files in a current directory with the names in the list. If you want to give them other names change the names in the list.

# To run: program_path input_file continuous_text_string_to_be_removed

echo ""
echo "Renaming files in the given directory..."

for f in $1/*.gff; do
	b=`basename $f $2.gff`
	d=`dirname $f`
	mv $f $d/$b.gff
done

echo "Done:)"

echo ""



