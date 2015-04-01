'''
Created on Mar 30, 2015

@authors: hliu, tjaraczewski, eotles
'''


def main():
    #Testing the functionality of the TCGA parser
    import parser as prs
    prad_tcga_filepath = 'Data/TCGA/PRAD/PRAD.uncv2.mRNAseq_raw_counts.txt'
    data = {_: dict() for _ in ["PRAD"]}
    data["PRAD"]["TCGA"] = prs.tcga(prad_tcga_filepath)
    data["PRAD"]["TCGA"].disp()
    
    data["PRAD"]["TCGA"] = prs.ccle(prad_tcga_filepath)
    data["PRAD"]["TCGA"].disp()


if __name__ == '__main__':
    main()
