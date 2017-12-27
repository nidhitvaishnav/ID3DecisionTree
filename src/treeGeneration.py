import numpy as np
import math
from anytree import Node
import copy
import random


class TreeGeneration:

#|-----------------------------------------------------------------------------|
# createDecisionTree
#|-----------------------------------------------------------------------------|
    def createDecisionTree(self, dataArr, headerList, classArr, classEntropy,\
                            treeNode, rootNodeCounter, parentNode):
        """
        This function creates decision tree
        """
        copyHeaderList= copy.deepcopy(headerList)
        #terminating condition
        if len(headerList) == 0:
            return treeNode 
#         #debug
#         print ('headerList = {} '.format(headerList))
#         #debug -ends
        
        #finding first split node (root node0
        splittingNodeHeader, entropyOne, entropyZero, counterClassOne,\
         counterClassZero=self.runID3(dataArr,\
                                            headerList, classArr, classEntropy)
#         #debug
#         print ('--------------------------------------------------------------')
#         print ('splittingNodeHeader = {} entropyOne = {}, entropyZero = {}'.\
#                         format(splittingNodeHeader, entropyOne, entropyZero))
#         print ('--------------------------------------------------------------')
#         #debug -ends
        
        #remove split node header and its data from modified lists
        splitNodeIndex = headerList.index(splittingNodeHeader)
 
        nodeClass0, nodeClass1 = self.assignClassAndPath(\
                                                dataArr=dataArr,\
                                                classArr=classArr,\
                                                splitNodeIndex=splitNodeIndex,\
                                                entropy0=entropyZero,\
                                                entropy1=entropyOne)
        #check for root node
        if rootNodeCounter == 0:                
            currentNode = Node(splittingNodeHeader, parent=None,\
                                path0=None, path1 = None,\
                                class0=nodeClass0, class1=nodeClass1,\
                                instanceClass0 = counterClassZero,\
                                instanceClass1 = counterClassOne)
        else:
            currentNode = Node(splittingNodeHeader, parent=parentNode, \
                                path0=None, path1 = None,\
                                class0=nodeClass0, class1=nodeClass1,\
                                instanceClass0 = counterClassZero,\
                                instanceClass1 = counterClassOne)
        #if nodeCounter -ends
        rootNodeCounter+=1
        #creating treeNode
        treeNode.append(currentNode)
        
        #linking current node with parent node
        if (parentNode!=None):
            parentNodeIndex = treeNode.index(parentNode)
#             #debug
#             print ('parentNodeIndex = {} '.format(parentNodeIndex))
#             #debug -ends
            if (treeNode[parentNodeIndex].class0==None and\
                 treeNode[parentNodeIndex].path0==None):
                treeNode[parentNodeIndex].path0=currentNode
            elif(treeNode[parentNodeIndex].class1==None and\
                 treeNode[parentNodeIndex].path1==None):
                treeNode[parentNodeIndex].path1=currentNode  
            #if -ends
        #if parentNode -ends
        
        rows, cols = np.shape(dataArr)
        headerList = copyHeaderList
        headerList.remove(splittingNodeHeader) 
        #check for entropyZero (left side of tree)
        if(entropyZero != 0):
            #adding all those rows who has 0 value in splitNode column in 
            #dataArr; and taking respective class values and creating new 
            #classArr0 and dataArr0
            dataArr0 = np.empty((0,cols))
            classArr0 = np.array([])
            for index, data in enumerate(dataArr):
                if data[splitNodeIndex]==0:
                    dataArr0=np.append(arr = dataArr0, values = [data],axis = 0)
                    classArr0=np.append(arr = classArr0, \
                                            values = [classArr[index]], axis=0)
                #if -ends
            #for -ends
            dataArr0 = np.delete(arr = dataArr0, obj=(splitNodeIndex), axis=1)
#             #debug
#             print ('dataArr0 = \n{} '.format(dataArr0))
#             print ('classArr0 = \n{}'.format(classArr0))
#             #debug -ends
          
            #call function recursively
            self.createDecisionTree(dataArr0, headerList, classArr0, classEntropy,\
                            treeNode,rootNodeCounter, parentNode = currentNode)              
        #if entropyZero -ends
#         #debug
#         print ('headerList = {} '.format(headerList))
#         #debug -ends 
        #check for entropyOne (right side of tree)    
        if(entropyOne != 0):
            #adding all those rows who has 0 value in splitNode column in 
            #dataArr; and taking respective class values and creating new 
            #classArr0 and dataArr0
            dataArr1 = np.empty((0,cols))
            classArr1 = np.array([])
            for index, data in enumerate(dataArr):
                if data[splitNodeIndex]==1:
                    dataArr1=np.append(arr = dataArr1, values = [data],axis = 0)
                    classArr1=np.append(arr = classArr1, \
                                            values = [classArr[index]], axis=0)
                #if -ends
            #for -ends
            dataArr1 = np.delete(arr = dataArr1, obj=(splitNodeIndex), axis=1)
#             #debug
#             print ('dataArr1 = \n{} '.format(dataArr1))
#             print ('classArr1 = \n{}'.format(classArr1))
#             #debug -ends
            #call function recursively
            self.createDecisionTree(dataArr1, headerList, classArr1, classEntropy,\
                            treeNode,rootNodeCounter, parentNode = currentNode)      
        #if entropyOne -ends
        return treeNode
#|------------------------createDecisionTree -ends-----------------------------|       
#|-----------------------------------------------------------------------------|
# runID3
#|-----------------------------------------------------------------------------|
    def runID3(self, dataArr,headerList, classArr, classEntropy):
        """
        Given function implements ID3 algorithm and creates a decision tree
        """
        # finding total rows and column of dataArr
        dataRows, dataCols = np.shape(dataArr)
        
        attributeGainArr = np.array([])
        entropyArr = np.empty(shape=[0,2])
        #for each attribute/column we are finding entropy with respect to class
        for col in range(0, dataCols):
            attributeArr = dataArr[:,col]
            #finding py
            attributeSigmaEntropy, entropyOne, entropyZero, counterClassOne,\
             counterClassZero =self.findAttributeEntropy(attributeArr,classArr, dataRows)
            #attributeGain
            attributeGain = classEntropy - attributeSigmaEntropy
            #storing attributeGain and entropies for each calculations
            attributeGainArr=np.append(arr = attributeGainArr, \
                                                    values = attributeGain)
            entropyArr = np.append(arr = entropyArr, values=[[entropyOne,\
                                                        entropyZero]], axis=0)
        #for col -ends
        
        #The node which gives maximum attributeGain is our splittingHeader
        maxAttributeGain = np.max(attributeGainArr)
        maxAttributeGainIndex =attributeGainArr.tolist().index(maxAttributeGain)
        splittingNodeHeader = headerList[maxAttributeGainIndex]
        entropyOne, entropyZero = entropyArr[maxAttributeGainIndex, :]

        return splittingNodeHeader, entropyOne, entropyZero, counterClassOne, counterClassZero        
#|------------------------runID3 -ends-----------------------------------------|    
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
#|-----------------------------------------------------------------------------|
# assignClassAndPath
#|-----------------------------------------------------------------------------|
    def assignClassAndPath(self, dataArr, classArr,splitNodeIndex, entropy0,\
                                                                    entropy1):
        """
        given function takes dataArr, classArr and entropies;
        It returns class and path values
        """
        class0Arr = np.array([])
        class1Arr = np.array([])

        #if entropy0==0, make path0 true, and assign respective class0 value
        if entropy0==0:    
            index0Arr = np.where(dataArr[:,splitNodeIndex]==0)
            for myIndex in index0Arr:
                class0Arr=np.append(class0Arr, classArr[myIndex])
            #for myIndex -ends
            sizeOfClass0Arr = class0Arr.shape
            #TODO: here for testing purpose we are printing class0 value as 2 if
            #no class assignment is found, but later, put none instead of 2
            class0 = 0 if np.array_equal(class0Arr, np.zeros(sizeOfClass0Arr)) else 2
            class0 = 1 if np.array_equal(class0Arr, np.ones(sizeOfClass0Arr)) else class0
        else:
            class0=None
        #if entropy0 -ends    
                
        #if entropy1==0, make path1 true, and assign respective class1 value         
        if entropy1==0:    
            index1Arr = np.where(dataArr[:,splitNodeIndex]==1)
            for myIndex in index1Arr:
                class1Arr = np.append(class1Arr, classArr[myIndex])
            #for myIndex -ends
            sizeOfClass1Arr = class1Arr.shape
            #TODO: here for testing purpose we are printing class1 value as 2 if
            #no class assignment is found 
            class1 = 0 if np.array_equal(class1Arr, np.zeros(sizeOfClass1Arr)) else 2
            class1 = 1 if np.array_equal(class1Arr, np.ones(sizeOfClass1Arr)) else class1
        else:
            class1=None
        #if entropy1 -ends             
        return class0, class1
#|------------------------assignClassAndPath -ends-----------------------------| 
#|-----------------------------------------------------------------------------|
# findLeafNode
#|-----------------------------------------------------------------------------|
    def findLeafNode(self, treeNodeList):
        """
        given function finds leafNodes of tree
        Input: treeNodeList (list of node type)
        Output: leafNodeList (list of node type)
        """
        leafNodeList = []
        for node in treeNodeList:
            if node.is_leaf:
                leafNodeList.append(node)
            #if node.is_leaf -ends
        #for node ends
        return leafNodeList
#|------------------------findLeafNode -ends----------------------------------|       
#|-----------------------------------------------------------------------------|
# createDecisionTree
#|-----------------------------------------------------------------------------|
    def createRandomDecisionTree(self, dataArr, headerList, classArr, classEntropy,\
                            treeNode, rootNodeCounter, parentNode):
        """
        This function creates decision tree
        """
        copyHeaderList= copy.deepcopy(headerList)
        #terminating condition
        if len(headerList) == 0:
            return treeNode 
        #if -ends
        dataRows, dataCols = np.shape(dataArr)
        
        #finding first split node (root node0
        splittingNodeHeaderList=self.selectRandomAttribute(headerList)

        #remove split node header and its data from modified lists
        splittingNodeHeader = splittingNodeHeaderList[0]
        splitNodeIndex = headerList.index(splittingNodeHeader)
        
        #for ends
        sigmaEntropy, entropyOne, entropyZero, counterClassOne,\
             counterClassZero=self.findAttributeEntropy(\
                                        attributeArr = dataArr[:,splitNodeIndex],\
                                        classArr = classArr,\
                                        totalInstance = dataRows)
        
        

 
        nodeClass0, nodeClass1 = self.assignClassAndPath(\
                                                dataArr=dataArr,\
                                                classArr=classArr,\
                                                splitNodeIndex=splitNodeIndex,\
                                                entropy0=entropyZero,\
                                                entropy1=entropyOne)
        #check for root node
        if rootNodeCounter == 0:                
            currentNode = Node(splittingNodeHeader, parent=None,\
                                path0=None, path1 = None,\
                                class0=nodeClass0, class1=nodeClass1,\
                                instanceClass0 = counterClassZero,\
                                instanceClass1 = counterClassOne)
        else:
            currentNode = Node(splittingNodeHeader, parent=parentNode, \
                                path0=None, path1 = None,\
                                class0=nodeClass0, class1=nodeClass1,\
                                instanceClass0 = counterClassZero,\
                                instanceClass1 = counterClassOne)
        #if nodeCounter -ends
        rootNodeCounter+=1
        #creating treeNode
        treeNode.append(currentNode)
        
        #linking current node with parent node
        if (parentNode!=None):
            parentNodeIndex = treeNode.index(parentNode)
#             #debug
#             print ('parentNodeIndex = {} '.format(parentNodeIndex))
#             #debug -ends
            if (treeNode[parentNodeIndex].class0==None and\
                 treeNode[parentNodeIndex].path0==None):
                treeNode[parentNodeIndex].path0=currentNode
            elif(treeNode[parentNodeIndex].class1==None and\
                 treeNode[parentNodeIndex].path1==None):
                treeNode[parentNodeIndex].path1=currentNode  
            #if -ends
        #if parentNode -ends
        
        rows, cols = np.shape(dataArr)
        headerList = copyHeaderList
        headerList.remove(splittingNodeHeader) 
        #check for entropyZero (left side of tree)
        if(entropyZero != 0):
            #adding all those rows who has 0 value in splitNode column in 
            #dataArr; and taking respective class values and creating new 
            #classArr0 and dataArr0
            dataArr0 = np.empty((0,cols))
            classArr0 = np.array([])
            for index, data in enumerate(dataArr):
                if data[splitNodeIndex]==0:
                    dataArr0=np.append(arr = dataArr0, values = [data],axis = 0)
                    classArr0=np.append(arr = classArr0, \
                                            values = [classArr[index]], axis=0)
                #if -ends
            #for -ends
            dataArr0 = np.delete(arr = dataArr0, obj=(splitNodeIndex), axis=1)
#             #debug
#             print ('dataArr0 = \n{} '.format(dataArr0))
#             print ('classArr0 = \n{}'.format(classArr0))
#             #debug -ends
          
            #call function recursively
            self.createDecisionTree(dataArr0, headerList, classArr0, classEntropy,\
                            treeNode,rootNodeCounter, parentNode = currentNode)              
        #if entropyZero -ends
#         #debug
#         print ('headerList = {} '.format(headerList))
#         #debug -ends 
        #check for entropyOne (right side of tree)    
        if(entropyOne != 0):
            #adding all those rows who has 0 value in splitNode column in 
            #dataArr; and taking respective class values and creating new 
            #classArr0 and dataArr0
            dataArr1 = np.empty((0,cols))
            classArr1 = np.array([])
            for index, data in enumerate(dataArr):
                if data[splitNodeIndex]==1:
                    dataArr1=np.append(arr = dataArr1, values = [data],axis = 0)
                    classArr1=np.append(arr = classArr1, \
                                            values = [classArr[index]], axis=0)
                #if -ends
            #for -ends
            dataArr1 = np.delete(arr = dataArr1, obj=(splitNodeIndex), axis=1)
#             #debug
#             print ('dataArr1 = \n{} '.format(dataArr1))
#             print ('classArr1 = \n{}'.format(classArr1))
#             #debug -ends
            #call function recursively
            self.createDecisionTree(dataArr1, headerList, classArr1, classEntropy,\
                            treeNode,rootNodeCounter, parentNode = currentNode)      
        #if entropyOne -ends
        return treeNode
#|------------------------createDecisionTree -ends-----------------------------|    
#|-----------------------------------------------------------------------------|
# selectRandomAttribute
#|-----------------------------------------------------------------------------|
    def selectRandomAttribute(self, headerList):
        """
        given function selects a random attribute and returns its value
        """
        selectedRandomAttribute = random.sample(headerList, k=1)
#         #debug
#         print ('selectedRandomAttribute = {} '.format(selectedRandomAttribute))
#         #debug -ends
        return selectedRandomAttribute

    
#|------------------------selectRandomAttribute -ends--------------------------|

#|-----------------------------------------------------------------------------|
# calculateAverageDepth
#|-----------------------------------------------------------------------------|
    def calculateAverageDepth(self,actualTreeList):
        """
        This function calculates AverageDepth of the tree using following formula:
        AverageDepth= Sum of depth of leaf nodes/Total number of leaf nodes
        """
        sum=0
        
        leafNodeList=self.findLeafNode(actualTreeList)
        totalLeafNodes=len(leafNodeList)
        for node in leafNodeList:
            
            depth=node.depth
            sum=sum+depth
            
        averageDepth=sum/totalLeafNodes
        return averageDepth
#|------------------------calculateAverageDepth -ends----------------------------------|            