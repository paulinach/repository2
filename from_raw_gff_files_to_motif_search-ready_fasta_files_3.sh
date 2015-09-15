#! /bin/bash

# Author: Paulina Chilarska

# this script does what it says, that is you feed it with raw gff data and it prepares it for motif search with NestedMICA (that is, if it works at all)

# to run your script you have to be in the directory containing your raw gff files

# first make some new directories where your files will go

mkdir -p clustered/
cd clustered/
mkdir -p FASTA_files/
cd FASTA_files/
mkdir -p split_into_300bp_chunks/
cd split_into_300bp_chunks/
mkdir -p filtered_for_repeating_chunks/
cd ..
cd ..
cd ..
echo ""

# then in a loop... 

for f in `ls *.gff`; do
                    b=`basename $f .gff`
                    echo "Clustering $b...";

# ...cluster probes

                    java gfftools.ClusterApplication -threshold 2500 $b.gff >clustered/${b}.clustered.gff;
                    
# and now extract and mask sequence and save as fasta

		echo "Extracting sequences for $b...";
                    java jkdb.DumpRegionsGFFApplication -db /home/LABS/pc414/Documents/RotationThree/Applications/dm3.2bit -mask HARD ${b}.gff >clustered/FASTA_files/${b}.fa 

# Splits long sequences into chunks of <= 300bp

        	echo "Splitting $b...";
                   java biotools.SplitSeqs -maxLength 300 clustered/FASTA_files/${b}.fa >clustered/FASTA_files/split_into_300bp_chunks/${b}.split.fa 

# and remove repeat-rich chunks

        	echo "Removing repeat-rich chunks from $b...";
                   java biotools.SeqFilter -minNonN 100 clustered/FASTA_files/split_into_300bp_chunks/${b}.split.fa >clustered/FASTA_files/split_into_300bp_chunks/filtered_for_repeating_chunks/${b}.split.filt.fa ;

		echo "Done :)"
		echo ""

done

echo ""







