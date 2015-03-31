filename = 'Data/TCGA/PRAD/PRAD.uncv2.mRNAseq_raw_counts.txt'

with open(filename,'r') as f:
    content = [x.strip('\n') for x in f.readlines()]
    names = content[0].split('\t');
    samples = []
    for idx,line in enumerate(content):
        if idx >= 1:
            data = line.split('\t')
            print data[0]
            samples.append(data[0])
            
    data_matrix = [[0 for x in range(len(names) - 1)] for x in range(len(samples))]
    
    for idx,line in enumerate(content):
        if idx >= 1:
            data = line.split('\t')
            data_matrix[idx - 1][0:(len(data)-1)] = [float(x) for x in data[1:len(data)]]
    print data_matrix[2][2]
