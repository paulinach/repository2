#! /bin/bash

# Author: Paulina Chilarska

# to be run on blades (i.e. you have to first copy it to blades)

# to run: program_path dataset_name no_of_processors output_filename_middle_words optional_x_in_input_folder_name

# e.g. running_nested_MICA_automated.sh cas 2 over1_TSS_overlapped x

# export path

echo ""

echo "Exporting PATH..."

export PATH=/users/tad26/software/nmica-0.8.0/bin:$PATH


# then run your motif search

for f in `ls filtered_for_repeating_chunks$4/$1.overlap.extended.clustered.split.filt.fa`; do
                    b=`basename $f .overlap.extended.clustered.split.filt.fa`;

echo "Initiating motif search for ${b}..."

nohup nminfer -numMotifs 5 -minLength 8 -maxLength 12 -revComp -threads $2 -backgroundModel background62-mel.xml -ensembleSize 500 -seqs filtered_for_repeating_chunks$4/${b}.overlap.extended.clustered.split.filt.fa -out ${b}.$3.xms 2>motif-finding-job-${b}.err >${b}-run1.log & 

echo "${b} motif search running."

	done
 
echo "Done :)"
echo ""





