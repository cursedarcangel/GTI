import os

def listChanges():
    print('\n' + 'The command for listing changes is *git status*' + '\n')
    repo = input('Where is the git repo that you want to see the changes in?\n')
    os.system('cd ' + repo)
    os.system('git status')
