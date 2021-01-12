import os

def commit(repo):
    print('\n' + 'The command for committing is *git commit -m "insert message here"*' + '\n')
    message = input('What should the commit message be?\n')
    os.system('cd ' + repo)
    os.system('git commit -m ' + '"' + message + '"')
