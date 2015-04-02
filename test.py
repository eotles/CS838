'''
Created on Mar 30, 2015

@authors: hliu, tjaraczewski, eotles
'''


def main():
    #Testing the functionality of the TCGA parser
    import parser as prs
    #The TCGA file below jut has data for prostate cancer - right?
    prad_tcga_filepath = 'Data/TCGA/PRAD/PRAD.uncv2.mRNAseq_raw_counts.txt'
    #Does the CCLE file below have data for all of the cancers we wish to look at?
    ccle_filepath = 'Data/CCLE/CCLE_Expression_Entrez_2012-09-29.txt'
    data = {_: dict() for _ in ["PRAD"]}
    data["PRAD"]["TCGA"] = prs.tcga(prad_tcga_filepath)
    data["PRAD"]["TCGA"].disp()
    
    data["CCLE"] = prs.ccle(ccle_filepath)
    data["CCLE"].disp()
    #print(data["PRAD"]["CCLE"].names[0])


if __name__ == '__main__':
    main()
