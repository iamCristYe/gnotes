# output:
# os.rename("61bef91f8d51eea10edac514cccfeaa0.mp4","2016_06_04_14_36_37_61bef91f8d51eea10edac514cccfeaa0.mp4")


import os
import datetime
import dateutil.parser
import shutil
from win32com.propsys import propsys, pscon

if __name__ == "__main__":
    PATH = "."

    for filename in os.listdir(PATH):
        # try:
        properties = propsys.SHGetPropertyStoreFromParsingName(
            os.getcwd() + "\\" + filename
        )
        dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
        if dt:
            newName = (
                (
                    dateutil.parser.parse(str(dt)) +
                    datetime.timedelta(hours=8)
                ).strftime("%Y_%m_%d_%H_%M_%S")
                + "_"
                + filename
            )
            #newName = "123.mp4"
            # print(newName)

            print("os.rename(\""+filename + "\",\"" + newName+"\")")
            #print(os.path.join(os.getcwd(), filename))
            #print(os.path.join(os.getcwd(), newName))

            #print(os.getcwd() + "\\" + filename)
            #print(os.getcwd() + "\\" + newName)

            # print((filename))
            # print((newName))
            #os.rename(filename, newName)
        # except OSError as err:
        #    print("OS Error: {0}".format(err))
