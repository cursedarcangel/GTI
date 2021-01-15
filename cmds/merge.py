import os

def merge(repo):
    print('\n' + 'The command for merging branches is *git merge (branch)*' + '\n')
    branch = input('What is the name of the branch that you want to merge?')

    os.system('cd ' + repo)
    os.system('git merge ' + branch)
