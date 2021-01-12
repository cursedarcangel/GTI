import os

def stashChanges(repo):
    print('\n' + 'The command for stashing changes is *git stash*' + '\n')
    os.system('cd ' + repo)
    os.system('git stash')
