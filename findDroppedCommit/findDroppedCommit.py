
import os
import sys
import subprocess
from subprocess import Popen, PIPE, STDOUT

def run_cmd2file(cmd):
    fdout = open("file_out.log", 'a')
    fderr = open("file_err.log", 'a')
    fdout.write(cmd)
    p = subprocess.Popen(cmd, stdout=fdout, stderr=fderr, shell=True)
    if p.poll():
        return
    p.wait()
    return


def start():
    file_object = open('file.txt', 'rU')
    try:
        for line in file_object:
            lineArrayByWhiteSpace = line.split(" ")
            singleCommand = 'git show ' + lineArrayByWhiteSpace[2]
            run_cmd2file(singleCommand)
    finally:
        file_object.close()

if __name__ == '__main__':
    start()