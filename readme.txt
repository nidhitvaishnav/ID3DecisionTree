
1. We have used Python 2.7 to implement decision tree using ID3 algorithm.
2. The code is written in Eclipse IDE. The project name is decisionTreeMLAssignment. It comprises src folder which contains 
   following .py files:

1) decisionTreeUI.py
2) myIO.py
3) treeGeneration.py
4) accuracyCalculation.py
5) pruningTree.py

   There is other folder named dataset which contains training_set.csv ,validation_set.csv and test_set.csv of both 
   datasets- dataset1 and dataset2.
   The program can be run by providing following four inputs as command line arguments.

   1) complete path of the training dataset
   2) complete path of the validation dataset
   3) complete path of the test dataset,
   4) pruning factor

   If command line arguments are not provided, it takes training_set.csv, validation_set.csv, test_set.csv of dataset1
   and pruning factor=0.1 by default.

3. decisionTreeUI.py should be run to run the entire algorithm.

4. We have used anytree package of python to implement tree data structure and pandas for reading csv files. 
   
5. After running, the program will output the decision tree and results.

6. For pruning, we are randomly selecting leaf nodes. After pruning them, the accuracy is calculated. This process is
   iterated for 100 times until the accuracy increases than the previous one. As the accuracy increases a bit, 
   the iterations are stopped.
   
   

