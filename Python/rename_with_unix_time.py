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

if __name__ == "__main__":
    PATH = "."
    LENMP4 = len("1482227010527.mp4")
    LENJPG = len("mmexport1482227010527.jpg")
    LENJPEG = len("mmexport1482227010527.jpeg") #for webp as well
    LENWXCAM = len("wx_camera_1482227010527.mp4")

    for filename in os.listdir(PATH):
        if len(filename) == LENMP4:
            timestamp = filename.split(".")[0]
        elif len(filename) == LENJPG and filename.startswith("mmexport"):
            timestamp = filename[len("mmexport"):-4]
        elif len(filename) == LENJPEG and filename.startswith("mmexport"):
            timestamp = filename[len("mmexport"):-5]
        elif len(filename) == LENWXCAM and filename.startswith("wx_camera_"):
            timestamp = filename[len("wx_camera_"):-4] 
        else:
            continue

       # ext = filename.split(".")[-1]
        newName = datetime.datetime.fromtimestamp(int(timestamp)/1e3).strftime("%Y-%m-%d_%H-%M-%S")
        newName = newName + "_" + filename # + "." + ext

        try:
            os.rename(filename, newName)
            print(filename + " -> " + newName)
        except OSError as err:
            print("OS Error: {0}{1} already exists.".format(err, newName))
