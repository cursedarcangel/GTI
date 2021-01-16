import sys
import os

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
    print('6. Exit GTI')
    print()

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
    print('3. See changes in a file')
    print('4. See all prior commits')

    choice = int(input())

    if choice == 1:
        from cmds import listdiff
        listdiff.listChanges(repo)
    elif choice == 2:
        from cmds import stash
        stash.stashChanges(repo)
    elif choice == 3:
        from cmds import diff
        diff.diff(repo)
    elif choice == 4:
        from cmds import log
        log.log(repo)

def branches():
    print('1. Checkout a branch')
    print('2. Delete a branch')
    print('3. Merge branches')

    choice = int(input())

    if choice == 1:
        from cmds import checkout
        checkout.checkout(repo)
    elif choice == 2:
        from cmds import deleteb
        deleteb.deleteBranch(repo)
    elif choice == 3:
        from cmds import merge
        merge.merge(repo)

def remote():
    print('1. Set up remote')
    print('2. Get changes from remote')
    print('3. Push local changes to remote')

    choice = int(input())
    if choice == 1:
        print('Setup ssh with github with this link: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh')
        print('What is the name of the github account that owns the repo that you are committing to?\n')
        name = input()
        print('What is the repo name?\n')
        repoName = input()
        os.system('git remote add origin https://github.com/' + name + '/' + repoName + '.git')
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
elif choice == 6:
    sys.exit()
