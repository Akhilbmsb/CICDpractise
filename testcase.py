import os
import pandas as pd

def findFailedStatus():
    found = False
    print("inside findfailedstatus func")
    dataset = pd.read_csv('output.csv')
    print("reading file")
    for i in range(len(dataset)):
        print("dataset",dataset)
        if(dataset.loc[i][6] == 'failed'):
            print("inside if")
            found = True
    return found

def mergeCodeToReleaseBranch():
    print('inside mergeCodeToRelease')
    os.system('git checkout main')
    print('inside checkout main')
    os.system('git pull origin main')
    print('inside pull origin main')
    os.system('git merge test2')
    print('inside merge test2')
    os.system('git add .')
    print('inside git add')
    os.system('git commit -m "Merge test2 into main"')
    print('inside inside commit')  
    os.system('git push origin main')
    print('inside push origin main')

# def runAllTests():
#     os.system('python -m pytest')git merge test2

    
def runOsCommand():
    # runAllTests()
    # print("inside runOsCommand func")
    testpassed = findFailedStatus()
    print('test-passed', testpassed)
    if (testpassed == False):
        mergeCodeToReleaseBranch()
    else:
        print("test case failed")   

runOsCommand()