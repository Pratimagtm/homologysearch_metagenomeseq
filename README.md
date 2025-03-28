# Code for HMMER homology search of metagenomic reads against a HMM of protein of interest

# install hmmer

conda install bioconda::hmmer

# Hmmer models used for copper protein of interest: 

PF04234.hmm  TIGR00914.1.HMM  TIGR01511.1.HMM  TIGR02698.1.HMM PF00403.hmm  PF05275.hmm  TIGR01386.1.HMM  TIGR01730.1.HMM  TIGR02937.1.HMM PF00440.hmm  PF05425.hmm  TIGR01387.1.HMM  TIGR01845.1.HMM PF02583.hmm  PF11604.hmm  TIGR01480.1.HMM  TIGR02044.1.HMM

# These Hmmmodels are available in pfam, tigrfam

## create local hmm database

cat PF00403.hmm  PF05275.hmm TIGR01386.1.HMM  TIGR01730.1.HMM  TIGR02937.1.HMM PF00440.hmm  PF05425.hmm TIGR01387.1.HMM  TIGR01845.1.HMM PF02583.hmm  PF11604.hmm TIGR01480.1.HMM  TIGR02044.1.HMM PF04234.hmm  TIGR00914.1.HMM  TIGR01511.1.HMM  TIGR02698.1.HMM > cuhmmdb

hmmpress cuhmmdb
# this creates binary files of the hmm database, which will be used to perform homology search with the sequence of interest

# Metagenomics sequences *.fasta files available as DNA sequences will be converted into six-frame translation of them as individual open reading frames in FASTA format. 
# syntax esl-traanslate input fasta file location > output (output fasta file location)
esl-translate input.fasta > output output.fasta

# update input.json with the hmm database location and output file from esl-translate

