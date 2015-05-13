'''
Created on Mar 30, 2015

@author: hliu, tjaraczewski,eotles
'''

import copy


#ParsedData Class
#Attributes:
#    samples - list of sample IDs (corresponding to rows of matrix)
#    names - list of column names (corresponding to columns of matrix + 1)
#    matrix - list of lists storing the data for each sample
class ParsedData(object):
    #Constructor
    def __init__(self, samples, names, matrix):
        self.samples = samples
        self.names = names
        self.matrix = matrix
    #Pretty print display
    def disp(self, no_show=True):
        if(no_show):
            print("%s samples, %s names" %(len(self.samples), len(self.names)))
            print("matrix size: %s x %s" %(len(self.matrix),len(self.matrix[0])))
        else:
            print("samples names: %s\ncolumn names: %s" %(self.samples, self.names))
            print("matrix:")
            for row in self.matrix:
                print("\t%s" %(row))

#TCGA data parsing function
#Parameters:
#    filename - the input data filepath
#Returns:
#    ParsedData object
def tcga(filename,):
    with open(filename,'r') as f:
        content = [x.strip('\n') for x in f.readlines()]
        #note: names includes the name of the sample column - thus is will be 1
        #more than the number of matrix columns.
        samples = content[0].split('\t')[1:]
        names = []
        data_matrix = []
        for idx,line in enumerate(content):
            if idx >= 2:
                line_data = line.strip().split('\t')
                names.append(line_data[0])
                data_matrix.append([float(x) for x in line_data[1:]])
        data_matrix =zip(*data_matrix)
        return(ParsedData(samples, names, data_matrix))

#CCLE data parsing function
#Parameters:
#    filename - the input data filepath
#Returns:
#    ParsedData object
def ccle(filename):
    #It is for .res file type. ARM-normalized mRNA expression
    with open(filename, 'r') as f:
        content = [x.strip('\n') for x in f.readlines()]
        samples = []
        data_matrix = []
        names = list()
        for idx,line in enumerate(content):
            line_data = line.strip().split('\t')
            #line 0 is version number
            #line 1 is matrix dimension
            #line 2 is sample names?
            if(idx == 2):
                samples = line_data[2:]
            #first line is version number
            #second line is matrix dimension
            elif(idx >= 3):
                names.append("%s" %(line_data[1]))
                data_matrix.append([float(x) for x in line_data[2:]])
        data_matrix = zip(*data_matrix)
        return(ParsedData(samples, names, data_matrix))

#Parsed data aligning function
#Parameters:
#    parsedDatas - a list of parsedData objects
#Returns:
#    alignedDatas - a list of aligned parsedData objects
def align(parsedDatas):
    alignedNames = copy.deepcopy(parsedDatas[0].names)
    
    #find names of genes shared between all of the parsedData
    for parsedData in parsedDatas:
        alignedNames = [name for name in alignedNames if name in parsedData.names]
    
    #loop through all parsedDatas and keep only aligned names in proper order
    alignedDatas = list()
    for parsedData in parsedDatas:
        idxs = [parsedData.names.index(name) for name in alignedNames]
        alignedSamples = parsedData.samples
        print("%s, %s" %(min(idxs), max(idxs)))
        print(len(parsedData.matrix[0]))
        alignedMatrix = [[line[idx] for idx in idxs] for line in parsedData.matrix]
        print(idxs)
        alignedDatas.append(ParsedData(alignedSamples, alignedNames, alignedMatrix))

    return(alignedDatas)