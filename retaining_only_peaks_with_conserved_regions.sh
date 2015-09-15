#! /bin/bash

# Author: Paulina Chilarska

# this script attempts to take a Drosophila conserved regions coordinates, and retain only those that happen to be inside peaks supplied as gff file. It then extends each TSS to create new peak.

# to run it you have to be in the directory containing your fileterd gff peak files

# to run type script_path into the command line

mkdir -p overlapped_with_conserved_regions/
mkdir -p overlapped_with_conserved_regions/extended/
mkdir -p overlapped_with_conserved_regions/extended/repeats_clustered/

for f in `ls *.gff`; do
                    b=`basename $f .gff`
                    echo "";

# print all records in $b.gff which overlap a record in drosophila_conserved_regions_file.gff (that is your conserved regions' genome coordinates)

echo "Calculating the overlap for $b..."

java gfftools.RetainOverlapping $b.gff /home/LABS/pc414/Desktop/Link_to_Documents/RotationThree/Results/GFF_files/drosophila_conserved_regions_fixed.dm3.gff >overlapped_with_conserved_regions/$b.overlap.gff

# now extend your peaks 250 bp upstream and 50 bp downstream of each of your conserved regions

echo "Extending peaks into both directions..."

cd overlapped_with_conserved_regions/

java gfftools.ExtendApplication $b.overlap.gff -fivePrime 250 -threePrime 50 >extended/$b.overlap.extended.gff

cd extended/

# remove repeats

echo "Removing repeats..."

java gfftools.ClusterApplication -threshold 250 $b.overlap.extended.gff >repeats_clustered/$b.overlap.extended.clustered.gff

cd ..
cd ..

echo "Done :)"

	done

echo ""





