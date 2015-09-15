#! /bin/bash

# Author: Paulina Chilarska

# this script attempts to take a Drosophila conserved regions coordinates, and retain only those that happen to be inside peaks supplied as gff file. It then extends each TSS to create new peak.

# to run it you have to be in the directory containing your fileterd gff peak files

# to run: script_path size_of_chunks_for_initial_clustering_in_bp

# e.g. script_path/ 150

mkdir -p clustered_before_overlap_with_conserved_regions/
mkdir -p clustered_before_overlap_with_conserved_regions/small_chunks_pruned/
mkdir -p clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/
mkdir -p clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/extended/
mkdir -p clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/extended/repeats_clustered/

for f in `ls *.gff`; do
	b=`basename $f .gff`
	echo "";

# print all records in $b.gff which overlap a record in drosophila_conserved_regions_file.gff (that is your conserved regions' genome coordinates)

	echo "Clustering $b into $1 bp chunks..."

	java gfftools.ClusterApplication -threshold $1 $b.gff >clustered_before_overlap_with_conserved_regions/$b.gff

# remove smaller chunks

	echo "Removing small chunks..."

	java gfftools.GFFGrep -minLength 20 clustered_before_overlap_with_conserved_regions/$b.gff >clustered_before_overlap_with_conserved_regions/small_chunks_pruned/$b.clustered.gff

	echo "Calculating the overlap for $b..."

java gfftools.RetainOverlapping clustered_before_overlap_with_conserved_regions/small_chunks_pruned/$b.clustered.gff /home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Results/GFF_files/drosophila_conserved_regions_fixed.dm3.gff >clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/$b.overlap.gff

# now extend your peaks 250 bp upstream and 50 bp downstream of each of your conserved regions

	echo "Extending peaks into both directions..."

	cd clustered_before_overlap_with_conserved_regions/small_chunks_pruned/overlapped_with_conserved_regions/

java gfftools.ExtendApplication $b.overlap.gff -fivePrime 250 -threePrime 50 >extended/$b.overlap.extended.gff

	cd extended/

# remove repeats

	echo "Removing repeats..."

java gfftools.ClusterApplication -threshold 250 $b.overlap.extended.gff >repeats_clustered/$b.overlap.extended.clustered.gff

	cd ..
	cd ..
	cd ..
	cd ..

	echo "Done :)"

done

echo ""





