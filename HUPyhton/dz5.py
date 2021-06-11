#!./venv/bin/python3
# Backup
# Sorry, this code is a mess... But it was written within an hour!
import argparse
import subprocess
import os

def get_args():
    parser = argparse.ArgumentParser("Hello! This is ultimate backup scpipt!")
    parser.add_argument("-d", "--dir", help="dir to backup")
    parser.add_argument("-f", "--file", help="file to backup")
    parser.add_argument("-o", "--output", help="archive name")
    return parser.parse_args()

def tar(dir, name):
    subprocess.call(f"tar -cf {name}.tar {dir}", shell=True)

def path(source):
    head, tail = os.path.split(source)
    if not tail:
        tail = head.split('/', 1)[-1]
        head = head.split('/', 1)[:-1]
    print(f"Your head'n'tail ")



if __name__ == "__main__":
    options = get_args()
    dir = options.dir
    file = options.file
    output = options.output


    if file:
        head, tail = os.path.split(file)
    elif dir:
        head, tail = os.path.split(dir)


    if file:
        if not head:
            if not output:
                tar(tail, tail)
            else:
                tar(tail, output)
        else:
            os.chdir(head)
            if not output:
                tar(tail, tail)
            else:
                tar(tail, output)
    else:
        if head.split('/', 1)[-1] == dir or head.split('/', 1)[-1] + "/" == dir:
            if not output:
                tar(head, head)
            else:
                tar(head, output)
        else:
            os.chdir(head)
            os.chdir("..")
            if not output:
                tar(head.split('/', 1)[-1], head.split('/', 1)[-1])
            else:
                tar(head.split('/', 1)[-1], output)
