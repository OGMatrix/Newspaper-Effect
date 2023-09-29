from os import walk
import os

def renameFiles():
    f = []
    for (dirpath, dirnames, filenames) in walk("images"):
        f.extend(filenames)
        break

    for file in f:
        os.rename('images/' + file, 'cache/images/' + file)

    for i, file in enumerate(f):
        os.rename('cache/images/' + file, f'images/{i}.png')
        
    return True