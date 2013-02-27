__author__ = 'takahiro'

import subprocess

def getConsoleResult():
    p = subprocess.Popen("ls -l",shell=True,stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    sout, serr = p.communicate()

    return sout.decode('utf-8').split("\n")

if __name__ == '__main__':
    s = getConsoleResult()
    for line in s:
        print line
else:
    pass
