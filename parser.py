'''
Created on Mar 30, 2015

@author: hliu, tjaraczewski,eotles
'''

class ParsedData(object):
    def __init__(self, samples, names, matrix):
        self.samples = samples
        self.names = names
        self.matrix = matrix
    
    def disp(self, show_matrix=False):
        print("%s samples: %s\n%s names: %s" %(len(self.samples), self.samples, len(self.names), self.names))
        print("matrix size: %s x %s" %(len(self.matrix),len(self.matrix[0])))
        
        if(show_matrix):
            for row in self.matrix:
                print(row)

#parsing function to take file and return ParsedData object
def tcga(filename):
    with open(filename,'r') as f:
        content = [x.strip('\n') for x in f.readlines()]
        #note: names includes the name of the sample column - thus is will be 1
        #more than the number of matrix columns.
        names = content[0].split('\t')
        samples = []
        data_matrix = []
        for idx,line in enumerate(content):
            if idx >= 1:
                line_data = line.split('\t')
                samples.append(line_data[0])
                data_matrix.append([float(x) for x in line_data[1:]]) 
        return(ParsedData(samples, names, data_matrix))