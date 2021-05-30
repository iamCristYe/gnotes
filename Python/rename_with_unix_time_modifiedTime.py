#!/usr/bin/env python3

"""
Rename files with the Unix time.
The files are in Wechat folder of Android OS:
    /Tencent/MicroMsg/WeiXin/


author: Gymgle
created at: 2016-12-20
updated at: 2019-08-22
"""

import os
import datetime
import pathlib

if __name__ == "__main__":
    PATH = "."

    for filename in os.listdir(PATH):
        # print(int(filename[:12]))
       # ext = filename.split(".")[-1]
        #newName = datetime.datetime.fromtimestamp(int(filename[:13])/1000).strftime("%Y-%m-%d_%H-%M-%S")
        # newName = newName + "_" + filename # + "." + ext
        fname = pathlib.Path(filename)
        newName = (datetime.datetime.fromtimestamp(
            int(fname.stat().st_mtime)).strftime("%Y-%m-%d_%H-%M-%S")) + "_" + filename

        try:
            #os.rename(filename, newName)
            print("os.rename(\""+filename + "\",\"" + newName+"\")")
        except OSError as err:
            print("OS Error: {0}{1} already exists.".format(err, newName))
