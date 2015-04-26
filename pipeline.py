'''
Created on Apr 19, 2015

@author: eotles
'''

class Pipeline(object):

    def __init__(self, parsedDataDict):
        self.parsedDataDict = parsedDataDict
    
    #standardize genes used in each data set   
    def standardizeData(self):
        for parsedData in self.parsedDataDict:
            pass
    
    #merge parsed data sets
    def merge(self):
        pass
    
    def normalize(self):
        