import os
import sys

if __name__ == "__main__":
    cmd = 'dir'
    os.system(cmd)
    res = os.popen(cmd, "r").read()
    # fp = open("dirlist_temp.txt", "r")
    fp = open("FINAL\\dirlist.txt", "w")
    fp.write(res)
    fp.close()
    print(res)