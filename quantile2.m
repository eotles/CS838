function [ data1_quantiled,data2_quantiled] = quantile2(data1,data2)
%QUANTILE Summary of this function goes here
%   Detailed explanation goes here
    length = max([size(data1,1) size(data2,1)]) * 3;
    Data = zeros(length,4);
    size(data1,2)
    for gene = 1:size(data1,2)
        tmp1 = repmat(data1(:,gene), floor(length / size(data1,1)) + 1 , 1);
        Data(:,1) = tmp1(1:length);
        tmp2 = repmat(data2(:,gene), floor(length / size(data2,1)) + 1 , 1);
        Data(:,2) = tmp2(1:length);  
        norm_data = quantilenorm(Data);
        data1_quantiled(:,gene) = norm_data(1:size(data1,1),1);
        data2_quantiled(:,gene) = norm_data(1:size(data2,1),2);        
    end
end