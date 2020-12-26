import os

def stashChanges():
    print('\n' + 'The command for stashing changes is *git stash*' + '\n')
    repo = input('What is the git repo that has the changes that you want to stash?\n')
    os.system('cd ' + repo)
    os.system('git stash')
