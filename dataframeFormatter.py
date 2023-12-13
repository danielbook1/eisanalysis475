import pandas as pd
import matplotlib.pyplot as plt
import os

SOURCE = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\good tests renamed\\"
DEST = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\good tests renamed\\ionic_resistance2.csv"

df = pd.DataFrame({'YSZ_COMP':[],
                   'N2':[],
                   'H2':[],
                   'TEMP':[],
                   'IONIC_RESISTANCE':[]
                   })


for filename in os.listdir(SOURCE):
    if '.csv' in filename:
        data = pd.read_csv(SOURCE + filename)
        x = data["Z\'(a)"]
        y = data["Z\'\'(b)"] * -1
        plt.plot(x,y)
        plt.axhline()
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.show()
        ionic_resistance = float(input())
        filename = filename[:-8]
        filename = filename.split('_')
        row = {'YSZ_COMP':[filename[0]],
               'N2':[filename[1]],
               'H2':[filename[2]],
               'TEMP':[filename[3]],
               'IONIC_RESISTANCE':[ionic_resistance]
               }
        df = pd.concat([df, pd.DataFrame(row)])
print(df)
df.to_csv(DEST,index=False)