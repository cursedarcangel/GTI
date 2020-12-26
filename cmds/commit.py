import os

def commit():
    print('\n' + 'The command for committing is *git commit -m "insert message here"*' + '\n')
    repo = input('Where is the repo that you want to commit to?\n')
    message = input('What should the commit message be?\n')
    os.system('cd ' + repo)
    os.system('git commit -m ' + message)
