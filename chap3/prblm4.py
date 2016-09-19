import os

def directorytree(x):
 for root, dirs, files in os.walk(x):
    path = root.split('/')
    print((len(path) - 1) * '- - - ', os.path.basename(root))
    for file in files:
        print(len(path) * '| | |', file)

directorytree('.')
