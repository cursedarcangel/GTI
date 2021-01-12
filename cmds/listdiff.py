import os

def listChanges(repo):
    print('\n' + 'The command for listing changes is *git status*' + '\n')
    os.system('cd ' + repo)
    os.system('git status')
