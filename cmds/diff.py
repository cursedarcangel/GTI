import os

def diff(repo):
    print('\n' + 'The command for seeing the changes to a file is *git diff (file)*' + '\n')

    fileN = input('What is the name of the file that you want to see the changes to?')

    os.system('cd ' + repo)
    os.system('git diff ' + fileN)
