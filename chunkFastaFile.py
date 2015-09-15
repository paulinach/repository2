#!/usr/bin/python

from Bio import SeqIO
import sys

(fastaFileName, outFileName, chunkSize) = sys.argv[1:4]

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

handle = open(fastaFileName, "rU")
handle2 = open(fastaFileName, "rU")


recordIds = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
rl = list(sorted(recordIds))

chunkSet = chunks(rl, int(chunkSize))

i=1
for ch in chunkSet:
    outputHandle = open(outFileName+"_"+str(i)+".faa", "w")
    for c in ch:
        out = ">"+recordIds[c].description
        outputHandle.write(str(out))
        outputHandle.write('\n')
        outputHandle.write(str(recordIds[c].seq))
        outputHandle.write('\n')
    outputHandle.close()
    i = i+1



handle.close()




