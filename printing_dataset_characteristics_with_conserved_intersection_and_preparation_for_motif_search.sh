#! /bin/bash

# Author: Paulina Chilarska

# this script calculates some statistics for gff peaks files and fasta files after intersection with a conserved regions file.

# the first two points below are calculated for a gff file before intersection with conserved regions and the next three refer to a fasta file after intersection

# to run it you have to be in the folder containing your intersection-ready gff files

echo ""
echo "Creating an empty results file..."
echo ""

resultsfilename=datasets_characteristics.txt

rm -f $resultsfilename
touch $resultsfilename


# now you do the intersection preceeded by 150bp clustering...

echo "Performing intersection with conserved regions file..."

/home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Applications/My_scripts/retaining_only_peaks_with_conserved_regions_with_initial_clustering.sh 150

# prepare resulting files for motif search

echo "Preparing the resulting files for motif search (includes conversion to fasta files)..."

cd clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/extended/repeats_clustered/

/home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Applications/My_scripts/from_raw_gff_files_to_motif_search-ready_fasta_files_3.sh 

cd ..
cd ..
cd ..
cd ..
cd ..

for f in `ls clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/extended/repeats_clustered/clustered/*.gff`; do
	b=`basename $f .gff`

# Calculate and print the number of peaks in your gff file
	
	echo "1. Total number of peak regions in clustered $b.gff is:" >>$resultsfilename
	wc -l <$f >>$resultsfilename
	echo "" >>$resultsfilename

# Calculate and print the total number of bases in your peaks

	echo "2. Number of bp covered by peaks in clustered $b.gff is:" >>$resultsfilename

	java gfftools.GFFCoverage $f >>$resultsfilename
	echo "" >>$resultsfilename

done

# ...and analyse the intersected fasta files

echo "Analysing the intersected fasta files..."
echo ""


for f in `ls clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/extended/repeats_clustered/clustered/FASTA_files/split_into_300bp_chunks/filtered_for_repeating_chunks/*.fa`; do
	b=`basename $f overlap.extended.clustered.split.filt.fa`

	echo "3. The total number of conserved blocks in $b.fa is:" >>$resultsfilename

# i.e the number of peaks in the after-intersection fasta file

	grep "chr" $f | wc -l >>$resultsfilename
	echo "" >>$resultsfilename

# point four refers to the number of bases covered by conserved regions after intersection so it means *all* the bases in the after-intersection fasta file

	echo "4. Number of covered bases in $b.fa is:" >>$resultsfilename

	java biotools.SeqLengths -total $f | grep ^Total | awk '{print $2}' >>$resultsfilename

	echo "" >>$resultsfilename

done

# go back to your gff files

for f in `ls *.gff`; do
	b=`basename $f .gff`

	echo "5. Number of peaks represented by at least one conserved block in clustered $b.gff is:" >>$resultsfilename

	java gfftools.RetainOverlapping $f /home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Results/GFF_files/drosophila_conserved_regions_fixed.dm3.gff | wc -l >>$resultsfilename
	
	echo "" >>$resultsfilename

done
echo "Done :)"

echo ""
