#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:51:29 2024

@author: pratima
"""
import os
import json
from os import path
import subprocess

def call_hmmer(hmmscan_arg):
    
    print('---- Start call hmmer, Creating .tab file ----')
    subprocess.call(hmmscan_arg, stdout=open(os.devnull, 'w'))
    print('----Call hmmer Ended----')
    #result of hmmer homology search will be saved in output file is created in same location as this python file in 'TAB' format
    
def run_hmmer(hmminputfile, eval, DB_path):

    print('---start run hmmer---')
    hmmscan_arg = (['hmmscan','--tblout', hmmoutputfile, '-E', str(eval), \
                    str(DB_path), hmminputfile])
    print('---Run hmmr ended---')
    call_hmmer(hmmscan_arg) 


# open and read json file
inputfilename = "input.json"

with open('input.json') as json_file:
    data = json.load(json_file)
    
# create a variable to hold dbPath value for later use.
eval = data["Hmmer"]["Max_eval"] 
DB_path = data["Hmmer"]["DB_path"]
readpath = data["Hmmer"]["Reads"]

# checks sequence file already exists
isfile = os.path.exists(readpath)

# create a list of sequence files
fastalist=[]
for f in os.listdir(readpath):
    if f.endswith(".fasta"):
        fastalist.append(f)


for file in fastalist:
    hmminputfile = readpath+file
    hmmoutputfile= file+ ".tab" 
    run_hmmer(hmminputfile, eval, DB_path) 