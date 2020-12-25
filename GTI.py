
def start():
    print('Welcome to GTI! What are you looking to do?')
    print()
    print('1. Clone a repo from GitHub')
    print('2. See a list of all changes in a git repo')
    print('3. Stash or delete changes')
    print('4. Commit to a repo')

start()

choice = int(input())

if choice == 1:
    from cmds import clone
    clone.cloneR()
elif choice == 2:
    from cmds import listdiff
    listdiff.listChanges()
