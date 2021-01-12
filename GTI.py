
with open('repo.txt', 'r+') as currentrepo:
    workingrepo = currentrepo.read()
    print('file opened')
    if workingrepo == '':
        print('What is the repo that you want to use?\n')
        repo = input()
        currentrepo.write(repo)
    repo = currentrepo.read()

def start():
    print('Welcome to GTI! What are you looking to do?\n')
    print('1. Clone a repo from GitHub')
    print('2. See a list of all changes in a git repo')
    print('3. Stash changes')
    print('4. Commit to a repo')
    print('5. Checkout a branch')

start()

choice = int(input())

if choice == 1:
    from cmds import clone
    clone.cloneR()
elif choice == 2:
    from cmds import listdiff
    listdiff.listChanges(repo)
elif choice == 3:
    from cmds import stash
    stash.stashChanges(repo)
elif choice == 4:
    from cmds import commit
    commit.commit(repo)
elif choice == 5:
    from cmds import checkout
    checkout.checkout(repo)
