load('Raw.mat');
load('Quantiled.mat');
load('pair_quantiled.mat');
load('z-score.mat');
z_score_data_50 = [CCLE_data_gbmlgg_zscore(1:50,:);CCLE_data_ov_zscore(1:50,:);TCGA_data_gbmlgg_zscore(1:50,:);TCGA_data_ov_zscore(1:50,:)];
[z_score_data_residual,z_score_data_pca_50] = pcares(z_score_data_50,2);
z_score_data_pca_50 = z_score_data_pca_50(:,1:2);

raw_data_50 = [CCLE_data_gbmlgg(1:50,:);CCLE_data_ov(1:50,:);TCGA_data_gbmlgg(1:50,:);TCGA_data_ov(1:50,:)];
[raw_data_residual,raw_data_pca_50] = pcares(raw_data_50,2);
raw_data_pca_50 = raw_data_pca_50(:,1:2);

quantiled_data_50 = [CCLE_data_gbmlgg_quantiled(1:50,:);CCLE_data_ov_quantiled(1:50,:);TCGA_data_gbmlgg_quantiled(1:50,:);TCGA_data_ov_quantiled(1:50,:)];
[quantiled_data_residual,quantiled_data_pca_50] = pcares(quantiled_data_50,2);
quantiled_data_pca_50 = quantiled_data_pca_50(:,1:2);

pair_quantiled_data_50 = [CCLE_data_gbmlgg_pair_quantiled(1:50,:);CCLE_data_ov_pair_quantiled(1:50,:);TCGA_data_gbmlgg_pair_quantiled(1:50,:);TCGA_data_ov_pair_quantiled(1:50,:)];
[pair_quantiled_data_residual,pair_quantiled_data_pca_50] = pcares(pair_quantiled_data_50,2);
pair_quantiled_data_pca_50 = pair_quantiled_data_pca_50(:,1:2);

Kmean(raw_data_50,4)