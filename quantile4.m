function [ data1_quantiled,data2_quantiled,data3_quantiled,data4_quantiled ] = quantile4(data1,data2,data3,data4)
%QUANTILE Summary of this function goes here
%   Detailed explanation goes here
    length = max([size(data1,1) size(data2,1) size(data3,1) size(data4,1)]) * 3;
    Data = zeros(length,4);
    size(data1,2)
    for gene = 1:size(data1,2)
        tmp1 = repmat(data1(:,gene), floor(length / size(data1,1)) + 1 , 1);
        Data(:,1) = tmp1(1:length);
        tmp2 = repmat(data2(:,gene), floor(length / size(data2,1)) + 1 , 1);
        Data(:,2) = tmp2(1:length);
        tmp3 = repmat(data3(:,gene), floor(length / size(data3,1)) + 1 , 1);
        Data(:,3) = tmp3(1:length);
        tmp4 = repmat(data4(:,gene), floor(length / size(data4,1)) + 1 , 1);
        Data(:,4) = tmp4(1:length);  
        norm_data = quantilenorm(Data);
        data1_quantiled(:,gene) = norm_data(1:size(data1,1),1);
        data2_quantiled(:,gene) = norm_data(1:size(data2,1),2);
        data3_quantiled(:,gene) = norm_data(1:size(data3,1),3);
        data4_quantiled(:,gene) = norm_data(1:size(data4,1),4);
        
    end
end
