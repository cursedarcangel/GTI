import os

def push(repo):
    print('\n' + 'The command for pushing your commits to the remote is *git push*' + '\n')

    os.system('cd ' + repo)

    os.system('git push')
