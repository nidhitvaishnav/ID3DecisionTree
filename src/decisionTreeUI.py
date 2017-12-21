import sys
from myIO import MyIO


class DecisionTreeUI:
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
        
      
#|------------------------decisionTreeUI -ends---------------------------------|    


if __name__ == '__main__':
    if len(sys.argv)>1  :
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
    decisionTree = DecisionTreeUI()
    decisionTree.decisionTreeUI(trainingPath, validationPath,\
                                        testingPath,pruningFactor)
