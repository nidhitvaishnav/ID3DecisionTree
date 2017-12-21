import pandas as pd
import numpy as np
from treeGeneration import TreeGeneration
import copy

class MyIO:
    """
    This class performs input - output tasks.
    """

#|-----------------------------------------------------------------------------|
# inputCSV
#|-----------------------------------------------------------------------------|
    def inputCSV(self, filePath):
        """
        given method takes csv file path as an input; reads csv file and
        return data in the form of numpy array
        """
        inputObj = pd.read_csv(filePath)
        inputArr = inputObj.values
        inputHeader = inputObj.columns.tolist()
        
        attributeArr, attributeHeader, classArr = \
                        self.segregateAttributesAndClass(inputArr, inputHeader)
        
        return attributeArr, attributeHeader, classArr
    
#|------------------------inputCSV -ends---------------------------------------|

#|-----------------------------------------------------------------------------|
# segregateAttributesAndClass
#|-----------------------------------------------------------------------------|
    def segregateAttributesAndClass(self, inputArr, inputHeader):
        """
        given function takes inputArr and inputHeader which contains attributes
        and class values,and
        returns attributeArr, attributeHeader and classArr
        """
        # finding total rows and column of dataArr
        dataRows, dataCols = np.shape(inputArr)
        # retrieving last column of dataArr
        classArr = inputArr[:, dataCols-1]
        
        #retrieving attributeArr
        attributeArr = inputArr[:, :dataCols-1]

        #retrieving attributeHeader
        attributeHeader = inputHeader[:dataCols-1]
        
        return attributeArr, attributeHeader, classArr
    
#|------------------------segregateAttributesAndClass -ends--------------------|
#|-----------------------------------------------------------------------------|
