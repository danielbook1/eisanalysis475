import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil

SOURCE = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\formatted tests\\"
GOOD_DEST = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\good tests\\"
BAD_DEST = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\bad tests\\"


for filename in os.listdir(SOURCE):
    data = pd.read_csv(SOURCE + filename)
    print(filename)
    print(data)
    x = data["Z\'(a)"]
    y = data["Z\'\'(b)"] * -1
    plt.plot(x,y)
    plt.axhline()
    plt.show()
    response = input()
    if 'b' in response:
        shutil.copy(SOURCE + filename, BAD_DEST + filename)
    else:
        shutil.copy(SOURCE + filename, GOOD_DEST + filename)