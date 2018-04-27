import pandas as pd

def parseAnnotation(file):
    df = pd.read_csv(file, sep = '\t', header = 0)

    #separate forward and reverse strand features
    forward = df.loc[df['STRAND'] == '+']
    reverse = df.loc[df['STRAND'] == '-']

    forwardFeatures = forward.drop(['SEQ_NAME','STRAND', 'ALIASES', 'DESCRIPTION','TXN_START','TXN_END','CDS_START','CDS_END','EXON_COUNT','EXON_STARTS','EXON_ENDS'])

    reverseFeatures = reverse.drop(['SEQ_NAME','STRAND', 'ALIASES', 'DESCRIPTION','TXN_START','TXN_END','CDS_START','CDS_END','EXON_COUNT','EXON_STARTS','EXON_ENDS'])

    return forwardFeatures, reverseFeatures
