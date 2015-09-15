#! /bin/bash

# Author: Paulina Chilarska

# This script shows logos for a file(s) supplied by the user.

# To run: program_path directory_containing_input_files

echo ""

cd $1

for f in `ls *.xms`; do
	b=`basename $f .xms`
	echo "Generating logos for $b (opens in a new window)...";
	echo "To display the next set of motifs press Ctrl+c."

	java net.derkholm.nmica.apps.MotifViewerApplication $f
	echo ""
	echo "Done:)"

done

echo ""

