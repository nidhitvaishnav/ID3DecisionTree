import numpy as np
from treeGeneration import TreeGeneration
import copy
from accuracyCalculation import AccuracyCalculation
import random



class PruningTree:
    
#|-----------------------------------------------------------------------------|
# findPrunedTree
#|-----------------------------------------------------------------------------|
    def findPrunedTree(self, pruningFactor, treeNodeList, validationData,\
            validationHeader, validationClassArr, initialvalidationAccuracy):
        """
        given function finds pruned tree based on pruning factor.
        Here, we are applying a heuristic logic, that we are allowing only leaf
        nodes to be pruned  
        Inputs: pruningFactor (double), treeNodeList (list of Node type),
                validationData (numpy array), validationHeader(list of string),
                validationClassArr (numpy array with same rows as validationdata)
                and initialValidationAccuracy ( double)
        Output: prunedTreeNodeList (list of Node type)
        """
        treeNodeListCopy = copy.deepcopy(treeNodeList)
        #finding total nodes of tree
        totalTreeNodes = len(treeNodeList)
        #finding number of nodes to prun by multiplying pruning factor with
        #total nodes of tree
        nNodesToPrun = (pruningFactor*totalTreeNodes)
#         #debug
#         print ('nNodesToPrun = {}\n '.format(nNodesToPrun.__class__))
#         #debug -ends
        nNodesToPrun = np.int(nNodesToPrun)
        print ('nNodsToPrun = {}'.format(nNodesToPrun))
#         #debug
#         print ('number of nodes to be pruned = {} '.format(nNodesToPrun))
#         #debug -ends
        for i in range(100):
            #taking back up of treeNodeList
            treeNodeList = copy.deepcopy(treeNodeListCopy)

            
            #HEURISTIC: we are pruning only leaf nodes
            #for that purpose, finding leaf nodes
            for j in range(nNodesToPrun):
                treeGeneration = TreeGeneration()
                leafNodeList = treeGeneration.findLeafNode(treeNodeList)
                #finding total number of leaves
                nLeafNode = len(leafNodeList)
                leafIndexList = np.arange(nLeafNode).tolist()
                #generating random nodes to prun, and removing them from the tree
#                  random.seed(0)
                pruningIndexList = random.sample(leafIndexList, k=1)
#                 pruningIndexList = random.sample(leafIndexList, k=nNodesToPrun)
    #         prunedTreeNodeList = copy.deepcopy(treeNodeList)
    
                for pruningIndex in pruningIndexList:
                    nodeToPrun = leafNodeList[pruningIndex]
                    parentNode = self.findImmidiateParent(nodeToPrun) 
                    #modifying parent node
                    parentIndex = treeNodeList.index(parentNode)
                    #Putting respective path values of parents as none
                    if treeNodeList[parentIndex].path0 == nodeToPrun:
                        #setting respective class values of parents
                        treeNodeList[parentIndex].path0 = None
                        #TODO: verify logic
                        #if class1's value is 1 than put class0 as 0, else reverse
                        if treeNodeList[parentIndex].class1 == 1:
                            treeNodeList[parentIndex].class0 = 0
                        else:
                            treeNodeList[parentIndex].class0 = 1
                    elif treeNodeList[parentIndex].path1 == nodeToPrun:
                        treeNodeList[parentIndex].path1 = None
                        #TODO: verify logic
                        #if class0's value is 1 than put class1 as 0, else reverse
                        if treeNodeList[parentIndex].class0 == 1:
                            treeNodeList[parentIndex].class1 = 0
                        else:
                            treeNodeList[parentIndex].class1 = 1
                    else:
                        print ("!------Error: found wrong parent--------!")
                    #if -ends
#                     #debug
#                     print ('nodeToPrun = {} '.format(nodeToPrun))
#                     print ('parent = {}'.format(parentNode))
#                     #debug -ends
                    treeNodeList.remove(nodeToPrun)          
                
                #for pruningIndex -ends
            #for j -ends
            
            accuracyCalculation = AccuracyCalculation()
            postPrunedAccuracy = accuracyCalculation.findAccuracy(\
                                                dataArr = validationData,\
                                                headerList = validationHeader,\

                                                classArr = validationClassArr,\
                                                treeNodeList = treeNodeList)
            if postPrunedAccuracy>initialvalidationAccuracy:
                break
        #for i -ends
        
#         #debug
#         print ('postPrunedAccuracy = {} '.format(postPrunedAccuracy))
#         #debug -ends
        
        return treeNodeList
#|------------------------findPrunedTree -ends---------------------------------| 
#|-----------------------------------------------------------------------------|
# findImmidiateParent
#|-----------------------------------------------------------------------------|
    def findImmidiateParent(self, currentNode):
        """
        
        """
        parentNode = None
        for i, myNode in enumerate(currentNode.ancestors):
            if i==len(currentNode.ancestors)-1:
                parentNode = myNode
            #if i -ends
        #for i, myNode -ends
        return parentNode
#|------------------------findImmidiateParent -ends----------------------------------|       