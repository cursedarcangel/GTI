import os

def log(repo):
    print('\n' + 'The command for seeing commits is *git log*' + '\n')

    os.system('cd ' + repo)
    os.system('git log')
