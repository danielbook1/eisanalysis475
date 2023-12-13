import csv
import os
import re

SOURCE = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\test 3\\"
DEST = "C:\\Users\\danie\\OneDrive\\Documents\\CPTS 475\\EIS Project\\data set 2\\formatted tests\\"

for filename in os.listdir(SOURCE):
    if ".z" in filename:
        with open(SOURCE + filename,'r') as srcfile:
            reader = csv.reader(srcfile)
            filename = filename[:-2] + '.csv'
            with open(DEST + filename,'w') as destfile:
                writer = csv.writer(destfile)
                count = 0
                for line in reader:
                    if count == 10:
                        line = re.split(r" +",line[0])[1:]
                        writer.writerow(line)
                    elif count > 10:
                        for i in range(len(line)):
                            line[i] = line[i].strip()
                        writer.writerow(line)
                    count += 1