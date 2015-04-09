import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def KMeans_wrapper(data_matrix,n_clusters=8):
    est=KMeans(n_clusters)
    est.fit(data_matrix)
    return est.labels_

def PCA_wrapper(data_matrix,n_dimensions=3):
    pca=PCA(n_dimensions)
    pca.fit(data_matrix)
    return pca
