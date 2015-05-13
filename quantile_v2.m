function [ TCGA_data_quantiled,CCLE_data_quantiled ] = quantile_v2( TCGA_data, CCLE_data )
%QUANTILE Summary of this function goes here
%   Detailed explanation goes here
    Data = zeros(size(TCGA_data,1),2);
    for gene = 1:size(TCGA_data,2)
        Data(:,1) = TCGA_data(:,gene);
        
        tmp = repmat(CCLE_data(:,gene), 1, floor(size(TCGA_data,1) / size(CCLE_data,1)) + 1);
        Data(:,2) = tmp(1:size(TCGA_data,1));
        norm_data = quantilenorm(Data);
        TCGA_data_quantiled(:,gene) = norm_data(:,1);
        CCLE_data_quantiled(:,gene) = norm_data(1:size(CCLE_data,1),2);
    end
end

