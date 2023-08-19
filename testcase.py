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
    os.system('cd ..')
    print('inside cd')
    os.system('cd mergefolder')
    print('inside cd to mergefolder')
    os.system('cd CICDpractise')
    print('inside cd to cicdpractise')
    os.system('git checkout main')
    print('inside checkout main')
    os.system('git pull origin main')
    print('inside pull origin main')
    os.system('git merge test2')
    print('inside merge test2')
    os.system('git add .')
    print('inside git add')
    os.system('git commit -m "Merge test2 into main"')
    print('inside  commit')  
    os.system('git pull')
    print('inside git pull')  
    os.system('git push main')
    print('inside push main')

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