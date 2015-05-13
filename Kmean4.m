function [] = Kmean4(X)
    idx = kmeans(X,4);
    size(idx)
    [sum(idx(1:50)    == 1) sum(idx(1:50)    == 2) sum(idx(1:50)    == 3) sum(idx(1:50)    == 4);
     sum(idx(51:100)  == 1) sum(idx(51:100)  == 2) sum(idx(51:100)  == 3) sum(idx(51:100)  == 4);
     sum(idx(101:150) == 1) sum(idx(101:150) == 2) sum(idx(101:150) == 3) sum(idx(101:150) == 4);
     sum(idx(151:200) == 1) sum(idx(151:200) == 2) sum(idx(151:200) == 3) sum(idx(151:200) == 4)]
end