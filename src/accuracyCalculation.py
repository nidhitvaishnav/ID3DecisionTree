
class AccuracyCalculation:
    
#|-----------------------------------------------------------------------------|
# findAccuracy
#|-----------------------------------------------------------------------------|
    def findAccuracy(self, dataArr, headerList, classArr, treeNodeList):
        """
        given function finds accuracy of the decision tree
        inputs: dataArr (numpy array), headerList (list), 
                classArray (numpy array), treeNodeList (list of Node type),
                leafNodeList (list of node type
        outputs:
        """
        nInstance, nAttributes = dataArr.shape

        correctAccuracyCount = 0
        incorrectAccuracyCount = 0
        for myIndex, myData in enumerate(dataArr):
            myClassVal = classArr[myIndex]
            matchFlag = self.matchInstanceWithTree(dataInstance = myData, \
                                                   headerList = headerList,\
                                                   instanceClassVal = myClassVal,\
                                                   treeNodeList=treeNodeList)
            if matchFlag:
                correctAccuracyCount+=1
            else:
                incorrectAccuracyCount+=1
            #if matchFlag -ends
        #for myIndex, myData ends
#         #debug
#         print ('+++++++++++++++++++++++++++++++++++++++')
#         print ('correctAccuracyCount = {}, incorrectAccuracyCount = {} '.format(\
#                                  correctAccuracyCount, incorrectAccuracyCount))
#         print ('+++++++++++++++++++++++++++++++++++++++')
#         #debug -ends
        dataAccuracy = float(correctAccuracyCount*100)/float(nInstance)
        
        
        return dataAccuracy
    
#|------------------------findAccuracy -ends-----------------------------------|    
#|-----------------------------------------------------------------------------|
# matchInstanceWithTree
#|-----------------------------------------------------------------------------|
    def matchInstanceWithTree(self, dataInstance, headerList, instanceClassVal,\
                                                                 treeNodeList):
        """
        given function checks whether dataInstance follows the decision tree
        prediction or not and returns appropriate boolean value
        """
        #find currentNode= rootnode (treeNode[0])
        #match currentNode.name with headerList, and get the column value
        #for the 1D array instance, check the value of instance[column]
        #based on that value, choose path from root (path0 or path1)
        #make child node as current node and so on
        #When this path ends, check its class. 
        #if class matches, return True, else return false
        
        currentNode=treeNodeList[0]
        currentNodeName = currentNode.name
        
        while True:
            dataHeaderIndex=headerList.index(currentNodeName)
            instancePathVal = dataInstance[dataHeaderIndex]
            if (instancePathVal==0):
                if currentNode.path0!=None:
                    nextNode = currentNode.path0
                else:
                    treeClassVal = currentNode.class0
                    if treeClassVal==instanceClassVal:
                        return True
                    else:
                        return False
                    #treeClassVal -ends
                #if currentnode.path0 -ends
            else:
                if currentNode.path1!=None:
                    nextNode = currentNode.path1
                else:
                    treeClassVal = currentNode.class1
                    if treeClassVal==instanceClassVal:
                        return True
                    else:
                        return False
                    #treeClassVal -ends
                #if currentNode.path1 -ends
            #if instancePathVal ends   
#             nextNode = [myNode for myNode in treeNodeList\
#                                          if (myNode.name==nextNodeName)]
            for myNode in treeNodeList:
                if (myNode==nextNode):
                    nextNode = myNode

            currentNode = nextNode
            currentNodeName = currentNode.name
        #while -ends        
            
    
#|------------------------matchInstanceWithTree -ends--------------------------|    