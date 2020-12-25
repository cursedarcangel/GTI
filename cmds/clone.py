import os

def cloneR():
    print('\n' + 'The command for cloning a repo is *git clone (insert url here) (insert destination here)*' + '\n')
    url = input('What is the url that you want to clone?\n')
    destination = input('Where do you want the repo to go?\n')
    command = ('git clone ' + url + ' ' + destination)
    os.system(command)
