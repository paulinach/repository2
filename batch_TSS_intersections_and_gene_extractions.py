#!/usr/bin/python

# This program takes a number of DMR files, intersects them with a TSS file and extracts genes from them.

# Author: Paulina Chilarska

# First working version saved on: 30/06/2011
# Last working version saved on: 

import subprocess
import os
import sys

# To use: program_path input_files
# E.g.: /Users/Paulina/MY_STUFF/PhD_project/Applications/My_scripts/batch_TSS_intersections_and_gene_extractions.py /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CG_DMRs/ALL_CG_h1_more_DMRs_above_55\%_no_headers.gff /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CG_DMRs/ALL_CG_imr90_DMRs_above_55\%_no_headers.gff /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CHG_DMRs/ALL_CHG_h1_more_DMRs_above_5\%_no_headers.gff /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CHG_DMRs/ALL_CHG_imr90_more_DMRs_above_5\%_no_headers.gff /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CHH_DMRs/ALL_CHH_h1_more_DMRs_above_5\%_no_headers.gff /Users/Paulina/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data_by_meth_direction/DMRs/NEW_CHH_DMRs/ALL_CHH_imr90_DMRs_above_5\%_no_headers.gff 

def TSS_intersection(file):
    outfile = file + "_intersected_with_TSSs.gff"
    out_file_handle = open(outfile, 'w');
    p = subprocess.Popen(['java', '-Xmx1800M', 'gfftools.RetainOverlapping', file, '/Users/paulina/Desktop/MY_STUFF/PhD_project/Lister_Pelizzola_BS-seq_data/ncbi36-tss.gff'],
    stdout=out_file_handle, shell=False)
    p.wait()
    out_file_handle.close()
    return None

def extract_genes(file):
    outfile = file + "_gene_names.txt"
    out_file_handle = open(outfile, 'w');
    p = subprocess.Popen(['java -Xmx1800M gfftools.GFFMine -attribute ensembl.gene_display_label ' + file + ' | sort | uniq'], stdout=out_file_handle, shell=True)
    p.wait()
    out_file_handle.close()
    return None

print '\nGoing into loop...\n'


list_of_file_names = (sys.argv[1:])


for file_name in list_of_file_names:
    TSS_intersection(file_name)
    extract_genes(file_name + "_intersected_with_TSSs.gff")
    print '\nDone for the following file: ' + file_name

print "Done.\n"




