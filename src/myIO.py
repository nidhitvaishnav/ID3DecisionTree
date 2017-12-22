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
# printTree
#|-----------------------------------------------------------------------------|
    def printTree(self, treeNodeList):
        """
        given function prints the tree nodes provided in the tree
        """
        print ('\n--------------- Decision Tree ----------------------------\n')
        #creating a stack of nodeList
        nodeStackList = []
        #we want to print all tree nodes
        for myNode in treeNodeList:
            #flag to check whether we are supposed to print class1 or class0
            class0PrintFlag = False
            #working on currentNode
            currentNode = copy.deepcopy(myNode)
            #we don't know where the stack ends, so using infinite loop
            while True:
                #count number of ancestors for indentation
                nAncestors = len(currentNode.ancestors)
                if nAncestors>0:
                    for nTab in range(nAncestors):
                        print("|    "),
                    #for nTab ends
                #if nAncestors -ends
                
                #check whether we wish to print class0 or class1
                if class0PrintFlag==False:
                    #if it is not a leaf node, put it in the stack for later;
                    #and go for actual next node which is myNode
                    #if it is a leaf node, let it be current node to process for
                    #class1; but in both cases, make clas0PrintFlag true.
                    if currentNode.class0==None:
                        print ("{} = {} ".format(currentNode.name, 0))
                        self.pushItem(stackList = nodeStackList, itemToPush =\
                                                                 currentNode)
                        class0PrintFlag=True
                        break                        
                    else:
                        print ("{} = {} ".format(currentNode.name, 0)),
                        print(": {}".format(currentNode.class0))
                        class0PrintFlag=True    
                    #if currentNode.class0 ends
                else:
                    #here we are getting popped nodes as current node;
                    #if currentNode is not a leaf node, print the value and let
                    #myNode be the next node
                    #but if currentNode is a leaf node, than check for
                    #empty stack condition, if not empty -> pop the node from
                    #stack and make it as currentNode; else it would be last 
                    #node in the tree, so break the loop
                    if currentNode.class1==None:
                        print ("{} = {} ".format(currentNode.name, 1))
                        break                        
                    else:
                        print ("{} = {} ".format(currentNode.name, 1)),
                        print(": {}".format(currentNode.class1))
                        if len(nodeStackList)!=0:
                            currentNode,nodeStackList = self.popItem(stackList \
                                                                = nodeStackList)
                        else:
                            break

                #if class0PrintFlag -ends
            #while -ends
        #for node -ends
            
        print ('\n----------------------------------------------------------\n')
#|------------------------printTree -ends--------------------------------------|   
#|-----------------------------------------------------------------------------|
# pushItem
#|-----------------------------------------------------------------------------|
    def pushItem(self, stackList, itemToPush):
        """
        it push the item in the stack list
        """
        stackList = stackList.insert(0, itemToPush)
        return stackList
#|------------------------pushItem -ends---------------------------------------|
#|-----------------------------------------------------------------------------|
# popItem
#|-----------------------------------------------------------------------------|
    def popItem(self, stackList):
        """
        it pops the item from the stack list and return the item and updated
        stackList
        """
        popedItem = stackList.pop(0)
        return popedItem, stackList
#|------------------------popItem -ends----------------------------------------|
#|-----------------------------------------------------------------------------|
# printAccuracyReport
#|-----------------------------------------------------------------------------|
    def printAccuracyReport(self, dataArr, accuracy, dataTypeStr,\
                                                     treeNodeList=None):
        """
        given function prints accuracy report and returns nothing
        """
        nInstance, nAttributes = dataArr.shape
        
        print ("Number of {} instances = {}".format(dataTypeStr, nInstance))
        if treeNodeList!=None:
            nNodes = len(treeNodeList)
            treeGeneration = TreeGeneration()
            leafNodeList = treeGeneration.findLeafNode(treeNodeList)
            #for myNode -ends
            nLeafNodes = len(leafNodeList)
#             totalNodes = nNodes+nLeafNodes
            print ("Total number of Nodes in the tree = {}".format(nNodes))
            print ("Number of leaf nodes in the tree = {}".format(nLeafNodes))
        #if treeNodeList -ends
        print ("number of {} attributes: {}".format(dataTypeStr, nAttributes))
        print ("Accuracy model on the {} dataset: {}\n".format(dataTypeStr,\
                                                                accuracy))
#|------------------------printAccuracyReport -ends----------------------------|        