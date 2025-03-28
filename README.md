# homologysearch_metagenomeseq
#Code for HMMER homology search of metagenomic reads against a HMM of protein of interest

#install hmmer

conda install bioconda::hmmer

Hmmer models used:
PF04234.hmm  TIGR00914.1.HMM  TIGR01511.1.HMM  TIGR02698.1.HMM
PF00403.hmm  PF05275.hmm  TIGR01386.1.HMM  TIGR01730.1.HMM  TIGR02937.1.HMM
PF00440.hmm  PF05425.hmm  TIGR01387.1.HMM  TIGR01845.1.HMM
PF02583.hmm  PF11604.hmm  TIGR01480.1.HMM  TIGR02044.1.HMM


#make hmmer db
cat PF00403.hmm  PF05275.hmm TIGR01386.1.HMM  TIGR01730.1.HMM  TIGR02937.1.HMM PF00440.hmm  PF05425.hmm TIGR01387.1.HMM  TIGR01845.1.HMM PF02583.hmm  PF11604.hmm TIGR01480.1.HMM  TIGR02044.1.HMM PF04234.hmm  TIGR00914.1.HMM  TIGR01511.1.HMM  TIGR02698.1.HMM > cuhmmdb

hmmpress cuhmmdb


#input.json file
db path home/pratima/Insync/pgautam1@umbc.edu/Google Drive/Cusick Lab/Metagenomic_analysis/Megan7_analysis/Copper_analysis/HMMmodels/cuhmm/cuhmmdb

def run_translate(hmminputfile):
    print('start translate')
    esl_trans= (['esl-translate', hmminputfile, transoutputfile])
    print('run translate')
    translate(transouputfile)
    
def translate(hmminputfile):
    print("--------translate---------")
    
    subprocess.call([esl_trans], stdout=open(os.devnull, 'w'))
    
    Terminal run for esl-translate
    esl-translate water.copper.fasta>output
    
Used sequence translated in 6 reading frames to run hmmscan with hmm model for copper genes

