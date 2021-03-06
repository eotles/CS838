'''
    Created on Mar 30, 2015
    @authors: hliu, tjaraczewski, eotles
    '''

import copy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from Algorithms import *
import scipy.io
import struct
import parser

def align(parsedDatas):
    alignedNames = copy.deepcopy(parsedDatas[0].names)
    #alignedNames = parsedDatas[0].names.copy()
    
    for parsedData in parsedDatas:
        alignedNames = [name for name in alignedNames if name in parsedData.names]
    
    alignedDatas = list()
    for parsedData in parsedDatas:
        idxs = [parsedData.names.index(name) for name in alignedNames]
        alignedSamples = parsedData.samples
        print("%s, %s" %(min(idxs), max(idxs)))
        print(len(parsedData.matrix[0]))
        alignedMatrix = [[line[idx] for idx in idxs] for line in parsedData.matrix]
        print(idxs)
        alignedDatas.append(parser.ParsedData(alignedSamples, alignedNames, alignedMatrix))
    
    #return(alignedNames)
    return(alignedDatas)



def main():
    #Testing the functionality of the TCGA parser
    import parser as prs
    
    print("Loading data....")
    #The TCGA file below jut has data for prostate cancer - right?
    #prad_tcga_filepath = 'Data/TCGA/GBM.transcriptome__ht_hg_u133a__broad_mit_edu__Level_3__gene_rma__data.data.txt'
    tcga_filepath = 'Data/TCGA/GBM.transcriptome__ht_hg_u133a__broad_mit_edu__Level_3__gene_rma__data.data.txt'
    #Does the CCLE file below have data for all of the cancers we wish to look at?
    ccle_filepath = 'Data/CCLE/CCLE_Expression_Entrez_2012-09-29.txt'
    #data = {_: dict() for _ in ["PRAD"]}
    data = {}
    data["TCGA"] = prs.tcga(tcga_filepath)
    data["CCLE"] = prs.ccle(ccle_filepath)
    print("Finish Loading data....")
    algn = align([data["TCGA"], data["CCLE"]])
    print(algn)
    print(len(algn))
#print(data["TCGA"].names)

#scipy.io.savemat('samples.mat', mdict={'samples': data["PRAD"]["TCGA"] .samples})
#scipy.io.savemat('genes.mat', mdict={'genes': data["PRAD"]["TCGA"] .names})

#print("Running PCA....")
#pca = PCA_wrapper(data["PRAD"]["TCGA"].matrix,3)
#pca_data = pca.transform(data["PRAD"]["TCGA"].matrix);
#scipy.io.savemat('pca_data_3d.mat', mdict={'pca_data_3d': pca_data})

#print("Running KMeans....")
#labels = KMeans_wrapper(pca_data,8)
#scipy.io.savemat('labels.mat', mdict={'labels': labels})

#data["PRAD"]["TCGA"].disp()

#data["CCLE"] = prs.ccle(ccle_filepath)
#print(data["CCLE"].names)

#genes dont seem to match
#algn = align([data["PRAD"]["TCGA"], data["CCLE"]])
#print(algn)
#print(len(algn))

#data["CCLE"].disp()
#print(data["PRAD"]["CCLE"].names[0])
#print("Computing Distance Matrix")
#X = data["PRAD"]["TCGA"].matrix[:100]

#estimators = {'k_means_iris_3': KMeans(n_clusters=3),
#'k_means_iris_8': KMeans(n_clusters=8),
#'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
#init='random')}

#for name, est in estimators.items():
#print(name)
#est.fit(X)
#labels = est.labels_
#actlabels = labels
#distanceMatrix = pdist(X)
#print("ploting......")
#dendrogram(linkage(distanceMatrix, method='complete'),
#color_threshold=0.3,
#leaf_label_func=lambda x: data["PRAD"]["TCGA"] .samples[x],
#leaf_font_size=6)

#f = plt.gcf()
#f.set_size_inches(8, 4);
#print("Showing plt.....")
#plt.show()
if __name__ == '__main__':
    main()