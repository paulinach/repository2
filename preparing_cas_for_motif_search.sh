#! /bin/bash

# Author: Paulina Chilarska

# this script does what it says, that is you feed it with raw gff data and it prepares it for motif search with NestedMICA (that is, if it works at all)

# first make some new directories where your files will go (change name of new directory every time you run the script)

#mkdir clustered_peaks_of_about_200kb/
#cd ..
#cd FASTA_files/
#mkdir peaks_of_about_200kb/
#cd  peaks_of_about_200kb/
#mkdir split_into_300bp_chunks/
#cd ..
#cd ..
#cd GFF_files/

# to run your script you have to be in Results/ directory)

# take your filtered data in a loop... 

for f in `ls /home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Results/GFF_files/clustered_peaks_of_about_200kb/cas.gff`; do
                    b=`basename $f .gff`
                    echo "Clustering $b...";

                    
# extract and mask sequence and save as fasta

		echo "Extracting sequences for $b...";
                    java jkdb.DumpRegionsGFFApplication -db /home/LABS/pc414/Documents/RotationThree/Applications/dm3.2bit -mask HARD /home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Results/GFF_files/clustered_peaks_of_about_200kb/${b}.gff >FASTA_files/peaks_of_about_200kb/${b}.fa ;

# Splits long sequences into chunks of <= 300bp

                 echo "Splitting $b...";
                   java biotools.SplitSeqs -maxLength 300 FASTA_files/peaks_of_about_200kb/${b}.fa >FASTA_files/peaks_of_about_200kb/split_into_300bp_chunks/${b}.split.fa ;

# and remove repeat-rich chunks

                   echo "Removing repeat-rich chunks from $b...";
                   java biotools.SeqFilter -minNonN 100 FASTA_files/peaks_of_about_200kb/split_into_300bp_chunks/${b}.split.fa >FASTA_files/peaks_of_about_200kb/split_into_300bp_chunks/filtered_for_repeating_chunks/${b}.split.filt.fa ;

echo "Done :)"

  done







