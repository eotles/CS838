%% Using only the first 50 samples from each
CCLE_gbm_50 = CCLE_data_gbmlgg(1:50,:); %% Data
CCLE_ov_50 = CCLE_data_ov(1:50,:);
TCGA_ov_50 = TCGA_data_ov(1:50,:);
TCGA_gbmlgg_50 = TCGA_data_gbmlgg(1:50,:);
RawData50 = [CCLE_gbm_50; CCLE_ov_50; TCGA_gbmlgg_50; TCGA_ov_50];
S_CCLEGBM_50 = cellstr(CCLE_samples_gbmlgg(1:50,:)); %% Sample labels
S_CCLEOV_50 = cellstr(CCLE_samples_ov(1:50,:));
S_TCGAGBM_50 = cellstr(TCGA_samples_gbmlgg(1:50,:));
S_TCGAOV_50 = cellstr(TCGA_samples_ov(1:50,:));
RawSamples50 = [S_CCLEGBM_50; S_CCLEOV_50; S_TCGAGBM_50; S_TCGAOV_50];

%% Mean Centering and Variance Scaling
X = RawData;       % Input data where it says RawData
numSamples = size(X,1);
Xmean = mean(X,1);
Xvar = std(X);
Xmeancentered = (X - repmat(Xmean, [numSamples 1])); %% This is mean centered
TCGA_data_ov_UV = rdivide(Xmeancentered,repmat(Xvar, [numSamples 1])); %% This adds variance scale

%% Quantile Normalization
function [ TCGA_data_quantiled,CCLE_data_quantiled ] = quantile( TCGA_data, CCLE_data )
%QUANTILE Summary of this function goes here
%   Detailed explanation goes here
    Data = zeros(size(CCLE_data,1),2);
    for gene = 1:size(TCGA_data,2)
        Data(:,1) = CCLE_data(:,gene);
        
        tmp = repmat(TCGA_data(:,gene), 1, floor(size(CCLE_data,1) / size(TCGA_data,1)) + 1);
        Data(:,2) = tmp(1:size(CCLE_data,1));
        norm_data = quantilenorm(Data, 'Median');
        CCLE_data_quantiled(:,gene) = norm_data(:,1);
        TCGA_data_quantiled(:,gene) = norm_data(1:size(TCGA_data,1),2);
    end
end

%% PCA script
[coeff1, score1] = princomp(X); %% X is data set
figure()
plot(score1(1:69,1),score1(1:69,2),'r+');  %% Numbers allow for distinguishing between samples
hold on
plot(score1(70:121,1),score1(70:121,2),'bo');
hold on
plot(score1(122:659,1),score1(122:659,2),'gx');
hold on
plot(score1(660:1252,1),score1(660:1252,2),'mo');
xlabel('1st Principal Component')
ylabel('2nd Principal Component');

%% HeatMap
%clust = clustergram(RawData50,'Standardize','row','Cluster','column','RowLabels',RawSamples50)
[idx,C] = kmeans(RawData50,4);
clust = clustergram(idx,'Standardize','none','Cluster','column','RowLabels',RawSamples50)