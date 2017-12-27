import sys
from myIO import MyIO
from treeGeneration import TreeGeneration
from accuracyCalculation import AccuracyCalculation


class RandomDecisionTreeUI:
    """
    This has one UI method, which calls every methods and provides 
    the final output
    """
#|-----------------------------------------------------------------------------|
# decisionTreeUI
#|-----------------------------------------------------------------------------|
    def decisionTreeUI(self, trainingPath, validationPath, testingPath,\
                                    pruningFactor):
        """
        given UI method performs following tasks:
        1. takes input
        2. finds decision tree using ID3 algorithm
        3. perform pruning
        4. provides output
        """
        #taking input
        myIO = MyIO()
        trainingData,trainingHeader,trainingClassArr = myIO.inputCSV(trainingPath)
        validationData, validationHeader, validationClassArr = myIO.inputCSV(validationPath)
        testingData, testingHeader, testingClassArr = myIO.inputCSV(testingPath)
        
        #finding entropy of the class
        treeGeneration=TreeGeneration()
        trainingEntropyOfClass = treeGeneration.findEntropyOfClass(trainingClassArr)
#         #debug
#         print ('entropyOfClass = {} '.format(trainingEntropyOfClass))
#         #debug -ends

        #calling createDecisionTree() to get treeNodeList
#         treeNodeList = treeGeneration.createDecisionTree(dataArr = trainingData,\
#                                          headerList = trainingHeader,\
#                                          classArr = trainingClassArr,\
#                                          classEntropy = trainingEntropyOfClass,\
#                                          treeNode = [], \
#                                          rootNodeCounter = 0,\
#                                          parentNode = None)
        treeNodeList = treeGeneration.createRandomDecisionTree(\
                                         dataArr = trainingData,\
                                         headerList = trainingHeader,\
                                         classArr = trainingClassArr,\
                                         classEntropy = trainingEntropyOfClass,\
                                         treeNode = [], \
                                         rootNodeCounter = 0,\
                                         parentNode = None)
#         #debug
#         print(RenderTree(node = treeNodeList[0], style=AsciiStyle()))
#         #debug -ends
        
        #printing tree
        myIO.printTree(treeNodeList)

        
        accuracyCalculation = AccuracyCalculation()
        prePruningTrainingAccuracy = accuracyCalculation.findAccuracy(\
                                                dataArr = trainingData,\
                                                headerList = trainingHeader,\
                                                classArr = trainingClassArr,\
                                                treeNodeList = treeNodeList)
        prePruningValidationAccuracy = accuracyCalculation.findAccuracy(\
                                                dataArr = validationData,\
                                                headerList = validationHeader,\
                                                classArr = validationClassArr,\
                                                treeNodeList = treeNodeList)
        prePruningTestingAccuracy = accuracyCalculation.findAccuracy(\
                                                dataArr = testingData,\
                                                headerList = testingHeader,\
                                                classArr = testingClassArr,\
                                                treeNodeList = treeNodeList)
         
        #printing accuracy report
        print ("-------------------------")
        print ("pre-Pruning accuracy")
        print ("-------------------------")
        myIO.printAccuracyReport(dataArr = trainingData,\
                                 accuracy = prePruningTrainingAccuracy,\
                                 dataTypeStr = "training",\
                                 treeNodeList = treeNodeList)
        myIO.printAccuracyReport(dataArr = validationData,\
                                 accuracy = prePruningValidationAccuracy,\
                                 dataTypeStr = "validation")
        myIO.printAccuracyReport(dataArr = testingData,\
                                 accuracy = prePruningTestingAccuracy,\
                                 dataTypeStr = "testing")
       
#         pruningTree = PruningTree()
#         prunedTreeNodeList = pruningTree.findPrunedTree(\
#                                 pruningFactor = pruningFactor,\
#                                 treeNodeList = treeNodeList,\
#                                 validationData = validationData,\
#                                 validationHeader = validationHeader,\
#                                 validationClassArr = validationClassArr,\
#                                 initialvalidationAccuracy = \
#                                                     prePruningValidationAccuracy)
#         
#         
#         postPruningTrainingAccuracy = accuracyCalculation.findAccuracy(\
#                                                 dataArr = trainingData,\
#                                                 headerList = trainingHeader,\
#                                                 classArr = trainingClassArr,\
#                                                 treeNodeList = prunedTreeNodeList)
#         postPruningValidationAccuracy = accuracyCalculation.findAccuracy(\
#                                                 dataArr = validationData,\
#                                                 headerList = validationHeader,\
#                                                 classArr = validationClassArr,\
#                                                 treeNodeList = prunedTreeNodeList)
#         postPruningTestingAccuracy = accuracyCalculation.findAccuracy(\
#                                                 dataArr = testingData,\
#                                                 headerList = testingHeader,\
#                                                 classArr = testingClassArr,\
#                                                 treeNodeList = prunedTreeNodeList)
#         
#         #printing accuracy report
#         print ("-------------------------")
#         print ("post-Pruning accuracy")
#         print ("-------------------------")
#         myIO.printAccuracyReport(dataArr = trainingData,\
#                                  accuracy = postPruningTrainingAccuracy,\
#                                  dataTypeStr = "training",\
#                                  treeNodeList = prunedTreeNodeList)
#         myIO.printAccuracyReport(dataArr = validationData,\
#                                  accuracy = postPruningValidationAccuracy,\
#                                  dataTypeStr = "validation")
#         myIO.printAccuracyReport(dataArr = testingData,\
#                                  accuracy = postPruningTestingAccuracy,\
#                                  dataTypeStr = "testing")
#          
        return treeNodeList
    
   
      
      
#|------------------------decisionTreeUI -ends---------------------------------|    


if __name__ == '__main__':
    if len(sys.argv)>1 and len(sys.argv)==4:
        print('system argm = {}'.format(sys.argv))
        trainingPath = sys.argv[1]
        validationPath = sys.argv[2]
        testingPath = sys.argv[3]
        pruningFactor = None
    elif len(sys.argv)==5:
        print('system argm = {}'.format(sys.argv))
        trainingPath = sys.argv[1]
        validationPath = sys.argv[2]
        testingPath = sys.argv[3]
        pruningFactor = float(sys.argv[4])
    else: 
#         trainingPath = '../tr/trDataset.csv'
        trainingPath = '../dataset/training_set.csv'
        validationPath = '../dataset/validation_set.csv'
        testingPath = '../dataset/test_set.csv'
        pruningFactor = 0.1
    #if -ends        
    decisionTree = RandomDecisionTreeUI()
    actualTreeList =decisionTree.decisionTreeUI(\
                                        trainingPath, validationPath,\
                                        testingPath,pruningFactor)
    treeGeneration= TreeGeneration()
    averageDepth=treeGeneration.calculateAverageDepth(actualTreeList)
    print("Average depth of decision tree using random splitting {} ".format(\
                                                                averageDepth))
#         print "no command line arguments specified. Please try again"
        