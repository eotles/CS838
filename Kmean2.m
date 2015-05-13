function [] = Kmean2(X)
    idx = kmeans(X,2);
    size(idx)
    [sum(idx(1:50)    == 1) sum(idx(1:50)    == 2);
     sum(idx(51:100)  == 1) sum(idx(51:100)  == 2);
     sum(idx(101:150) == 1) sum(idx(101:150) == 2);
     sum(idx(151:200) == 1) sum(idx(151:200) == 2)]
end