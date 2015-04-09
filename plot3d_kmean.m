load('genes.mat')
load('labels.mat')
load('samples.mat')
load('pca_data_3d.mat')
S = repmat([10,10,10],numel(pca_data_3d),1);
%C = repmat([1,2,3],numel(X),1);
scatter3(pca_data_3d(:,1),pca_data_3d(:,2),pca_data_3d(:,3),10*ones(size(pca_data_3d(:,1))),labels)