#This is the control script to call RNAse Y cleavage sites from
#Rend seq data

from parseWig import parseWig
from parseAnnotation import parseAnnotation
import pandas as import pd
import os


#import wig file name list
cwd = str(os.getcwd())
with open (cwd + '/wtNames.txt', 'r') as f:
    wtFiles = f.readlines()
with open (cwd + '/pnpANames.txt', 'r') as f:
    pnpaFiles = f.readlines()
with open (cwd + '/rnaseJNames.txt', 'r') as f:
    rnaseJFiles = f.readlines()
with open (cwd + '/rnaseYNames.txt', 'r') as f:
    rnaseYFiles = f.readlines()
with open (cwd + '/5exoNames.txt', 'r') as f:
    fiveExoFiles = f.readlines()


#parse wigs

#import annotation file.

#call peaks and sort by gene
