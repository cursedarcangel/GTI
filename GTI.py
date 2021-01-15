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
    print('1. Commit to a repo')
    print('2. Add changed files to be committed')

    choice = int(input())

    if choice == 1:
        from cmds import commit
        commit.commit(repo)
    elif choice == 2:
        from cmds import add
        add.add(repo)

def changes():
    print('1. See a list of changed files')
    print('2. Stash changes')

    choice = int(input())

    if choice == 1:
        from cmds import listdiff
        listdiff.listChanges(repo)
    elif choice == 2:
        from cmds import stash
        stash.stashChanges(repo)

def branches():
    print('1. Checkout a branch')

    choice = int(input())

    if choice == 1:
        from cmds import checkout
        checkout.checkout(repo)

def remote():
    print('1. Set up remote')
    print('2. Get changes from remote')
    print('3. Push local changes to remote')

    choice = int(input())
    if choice == 1:
        pass
    elif choice == 2:
        from cmds import pull
        pull.pull(repo)
    elif choice == 3:
        from cmds import push
        push.push(repo)

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
