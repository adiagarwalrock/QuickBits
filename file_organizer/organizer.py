import sys
from stat import *
import os
import shutil


def folder_exists(folder_name):
    if folder_name in list_folder():
        return True
    print(folder_name, "does not eists!")
    if create_folder(folder_name):
        return True
    return False


def create_folder(folder_name):
    os.mkdir(os.path.join(path, folder_name))
    print("Created: ", folder_name)
    return True


def move_file(source, destination):
    print("SOURCE: ", source)
    print("DESTINATION: ", destination)
    origin = os.path.join(path, source)
    target = os.path.join(path, destination)
    print("ORIGIN PATH: ", origin)
    print("TRGET PATH: ", target)
    # if folder_exists(path):
    if folder_exists(destination):
        try:
            shutil.move(origin, target)
            print("Moved: ", source, "-->", target)
            return True
        except Exception as e:
            print(e)
            return False


def list_files():
    all_items = os.listdir(path)
    global files
    files = []

    for item in all_items:
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)

    return files


def list_folder():
    all_files = os.listdir(path)
    global folders
    folders = []

    for item in all_files:
        if os.path.isdir(os.path.join(path, item)):
            folders.append(item)

    return folders


def category_files():
    from category import categories

    for item in list_files():
        ext = string.lower(item.split('.')[-1])
        source = item
        print("SOURCE ITEM: ", source)

        if ext in categories['documents']:
            target = 'Documents'

        elif ext in categories['videos']:
            target = 'Videos'

        elif ext in categories['images']:
            target = 'Pictures'

        elif ext in categories['softwares']:
            target = 'Softwares'

        elif ext in categories['compressed']:
            target = 'Compressed'

        elif ext in categories['programs']:
            target = 'Programs'

        else:
            target = 'Others'
        
        if move_file(source, target):
                print(target, '-->', item)
        else:
            continue
        
        print('################')
        print("")


if __name__ == '__main__':
    path = 'C:/Users/adity/Downloads'
    category_files()
    exit()
