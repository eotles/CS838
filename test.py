'''
Created on Mar 30, 2015

@authors: hliu, tjaraczewski, eotles
'''

#Testing the functionality of the TCGA parser
import parser as prs
data = {_: dict() for _ in ["PRAD"]}
data["PRAD"]["TCGA"] = prs.tcga('Data/TCGA/PRAD/PRAD.uncv2.mRNAseq_raw_counts.txt') 
data["PRAD"]["TCGA"].disp()

