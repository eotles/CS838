'''
Created on Mar 30, 2015

@authors: hliu, tjaraczewski, eotles
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

def main():
    #Testing the functionality of the TCGA parser
    import parser as prs
    print("Loading data....")
    #The TCGA file below jut has data for prostate cancer - right?
    prad_tcga_filepath = 'Data/TCGA/PRAD/PRAD.uncv2.mRNAseq_raw_counts.txt'
    #Does the CCLE file below have data for all of the cancers we wish to look at?
    ccle_filepath = 'Data/CCLE/CCLE_Expression_Entrez_2012-09-29.txt'
    data = {_: dict() for _ in ["PRAD"]}
    data["PRAD"]["TCGA"] = prs.tcga(prad_tcga_filepath)
    #data["PRAD"]["TCGA"].disp()
    
    #data["CCLE"] = prs.ccle(ccle_filepath)
    #data["CCLE"].disp()
    #print(data["PRAD"]["CCLE"].names[0])
    print("Computing Distance Matrix")
    X = data["PRAD"]["TCGA"].matrix[:100]
    distanceMatrix = pdist(X)
    
    estimators = {'k_means_iris_3': KMeans(n_clusters=3),
        'k_means_iris_8': KMeans(n_clusters=8),
            'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
                                            init='random')}
    for name, est in estimators.items():
        print(name)
        est.fit(X)
        labels = est.labels_
        actlabels = labels

        print("ploting......")
        dendrogram(linkage(distanceMatrix, method='complete'),
                   color_threshold=0.3,
                   leaf_label_func=lambda x: 'O' * (actlabels[x] + 1),
                   leaf_font_size=6)
    
        f = plt.gcf()
        f.set_size_inches(8, 4);
        print("Showing plt.....")
        plt.show()
if __name__ == '__main__':
    main()
