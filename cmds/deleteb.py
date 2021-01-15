import os

def deleteBranch(repo):
    print('\n' + 'The command for deleting a branch is *git branch -d (branch name)*' + '\n')

    print('What is the name of the branch that you want to delete?\n')

    name = input()

    os.system('cd ' + repo)
    os.system('git branch -d ' + name)
