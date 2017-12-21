import math
from anytree import Node


class TreeGeneration:

  
#|-----------------------------------------------------------------------------|
# findEntopyOfClass
#|-----------------------------------------------------------------------------|
    def findEntropyOfClass(self, classArr):
        """
        given function takes data array, in which last column will be the class
        label attribute, which is given in the boolean form
        The output of given function is entropy of class in double data type
        """
        #initializing counters
        countZero = 0
        countOne = 0
        #finding total zeros and ones from class
        for data in classArr:
            if data==0:
                countZero+=1
            elif data==1:
                countOne+=1
            else:
                print ("Input is not proper")
            #if data -ends
        #for data -ends

        classEntropy = self.calculateEntropy(positiveVal = countOne,\
                                              negativeVal = countZero)
        
        return classEntropy
#|------------------------findEntopyOfClass -ends------------------------------|   
#|-----------------------------------------------------------------------------|
# findAttributeEntropy
#|-----------------------------------------------------------------------------|
    def findAttributeEntropy(self, attributeArr, classArr, totalInstance):
        """
        given function takes attribute array and class array; calculate 
        py and returns it in form of double variable
        """
        #finding rows 
        #initializing counters
        #Ex. for counterOneOne firstOne is for attribute=1, 
        # second one is for class=1
        counterOneOne = 0
        counterOneZero = 0
        counterZeroOne = 0
        counterZeroZero = 0
        
        # for each distinct attribute values its corresponding distinct values
        # of class labels are counted
        for index, atrValue in enumerate(attributeArr):
            if atrValue==1 and classArr[index]==1:
                counterOneOne+=1
            elif atrValue==1 and classArr[index]==0:
                counterOneZero+=1
            elif atrValue==0 and classArr[index]==1:
                counterZeroOne+=1
            elif atrValue==0 and classArr[index]==0:
                counterZeroZero+=1
            #if atrValue -ends
        #for index, atrValue -ends

        #finding sigma entropy
        entropyOne = self.calculateEntropy(positiveVal = counterOneOne,\
                                            negativeVal = counterOneZero) 
        entropyZero = self.calculateEntropy(positiveVal = counterZeroOne,\
                                             negativeVal = counterZeroZero)   

        sigmaEntropy=(float((counterOneOne+counterOneZero))/float(totalInstance\
                        ))*entropyOne + (float((counterZeroOne+counterZeroZero)\
                                       )/float(totalInstance))*entropyZero
    
        counterClassOne = counterOneOne+counterZeroOne
        counterClassZero = counterZeroZero+counterOneZero 
        return sigmaEntropy, entropyOne, entropyZero, counterClassOne, counterClassZero
#|------------------------findAttributeEntropy -ends---------------------------|     

#|-----------------------------------------------------------------------------|
# calculateEntropy
#|-----------------------------------------------------------------------------|
    def calculateEntropy(self, positiveVal, negativeVal):
        """
        Input: positiveValue, nagative values(integer);    Output:entropy(float) 
        Formula
        Entropy = -(p/(p+n))log2(p/(p+n)) - (n/(p+n))log2(p/(P+n))
        """
        entropy=0
        #checking corner case where positiveVal and negativeVal are zero
        if (positiveVal==0 and negativeVal==0):
            return entropy
        #finding entropy
        x = float(positiveVal/float(positiveVal+negativeVal))
        y = float(negativeVal/float(positiveVal + negativeVal))

        #finding entropy,if x=0, find entropy of y,if y=0, find entropy of x,
        # else use the formula  
        if x==0:
            entropy = -y*math.log(y,2)
        elif y==0:
            entropy = -x*math.log(x,2)
        else:
            entropy = -(x*math.log(x,2))-(y*math.log(y,2))
        
        return entropy
    
#|------------------------calculateEntropy -ends-------------------------------|  
     
