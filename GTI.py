import sys

with open(sys.argv[1], 'r+') as currentrepo:
    workingrepo = currentrepo.read()
    print(workingrepo)
    if workingrepo == '':
        print('What is the repo that you want to use?\n')
        repo = input()
        currentrepo.write(repo)
    repo = currentrepo.read()
print('Welcome to GTI! What are you looking to do?')
def start():
    print('1. Clone a repo from GitHub')
    print('2. Commits')
    print('3. See changes')
    print('4. Branches')
    print('5. Remote stuff')

start()

choice = int(input())

def commits():
    pass

def changes():
    pass

def branches():
    pass

def remote():
    pass

if choice == 1:
    from cmds import clone
    clone.cloneRepo()
elif choice == 2:
    commits()
elif choice == 3:
    changes()
elif choice == 4:
    branches()
elif choice == 5:
    remote()
