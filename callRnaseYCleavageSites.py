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
wtData = pd.DataFrame()
pnpaData = pd.DataFrame()
rnaseJData = pd.DataFrame()
rnaseYFiles = pd.DataFrame()
fiveExoFiles = pd.DataFrame()

for name in wtFiles:
    d = parseWig(name)
    wtData.append(d)

for name in pnpaData:
    d = parseWig(name)
    pnpaData.append(d)

for name in rnaseJData:
    d = parseWig(name)
    rnaseJData.append(d)

for name in rnaseYFiles:
    d = parseWig(name)
    rnaseYData.append(d)

for name in fiveExoFiles:
    d = parseWig(name)
    fiveExoFiles.append(d)

#import annotation file.
annotationFile = '/Users/eagb/Dropbox (MIT)/LiLab/For_Ethan_B_subtilis_nucleases/B_subtilis/CDS_168_detailed_Mochi_20180411.txt'

forwardFeatures, reverseFeatures = parseAnnotation(annotationFile)

#call peaks and sort by gene
