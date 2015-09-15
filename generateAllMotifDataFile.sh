#!/bin/bash

#ls *.data|awk '{print "awk '\''\{print \$1-5500,\$3,\""$1"\"\}'\'' ",$1,">>allmotif.data"}'|sed 's/\.\.\///1' |sed 's/\.motif/ motif/'|sed 's/\.data//'|sh

rm -f allmotif.data

ls *.data|awk '{print "awk '\''{print $1-5500,$3,\""$1"\"}'\'' ",$1,">>allmotif.data"}'|sed 's/\.\.\///1' |sed 's/\.motif/ motif/'|sed 's/\.data//' | sh
#ls *.data|awk '{print "awk '\''{print $1-5500,$3,\""$1"\"}'\'' ",$1,">>allmotif.data"}'|sed 's/\.\.\///1' |sed 's/\.motif/ motif/'|sed 's/\.data//'


