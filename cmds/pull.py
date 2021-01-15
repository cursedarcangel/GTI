import os

def pull(repo):
    print('\n' + 'The command for getting the latest changes from the remote is *git pull*' + '\n')

    os.system('cd ' + repo)

    os.system('git pull')
