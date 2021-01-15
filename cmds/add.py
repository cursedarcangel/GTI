import os

def add(repo):
    print('\n' + 'The command for adding files to be committed is *git add (file)*' + '\n')
    os.system('cd ' + repo)
    os.system('git status')
    print('What files do you want to add?(enter * * to stop adding)')

    files = []

    while True:
        addThis = input()
        if addThis == ' ':
            break
        else:
            files.append(addThis)

    for addThis in files:
        os.system('git add ' + addThis)

