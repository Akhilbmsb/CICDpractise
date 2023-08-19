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
    print('Pulled changes from remote main branch')

    os.system('git merge test2')
    print('Merged test2 into main branch')

    os.system('git add .')
    print('Added changes to commit')

    os.system('git commit -m "Merge test2 into main"')
    print('Committed changes')

    
    os.system('git pull origin main')
    print('Pulled changes after merging and committing')

    push_result = os.system('git push origin main')
    if push_result != 0:
        print("Error pushing to main branch")



    
def runOsCommand():
    testpassed = findFailedStatus()
    print('test-passed', testpassed)
    if (testpassed == False):
        mergeCodeToReleaseBranch()
    else:
        print("test case failed")   

runOsCommand()