import os

def checkout(repo):
    print('\n' + 'The command for checking out a branch is *git checkout (branch name)* plus a -b in between checkout and the branch name if you are creating a branch' + '\n')
    new = input('Is it a new branch or not (y/n)\n')
    name = input('What is the branch called, or what should it be called\n')

    os.system('cd ' + repo)

    if 'y' in new:
        os.system('git checkout -b ' + name)
    else:
        os.system('git checkout ' + name)
