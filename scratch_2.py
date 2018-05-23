import os
import fnmatch
dir="/home/mjakub/Desktop/asd/"
for i in range(len(fnmatch.filter(os.listdir(dir), '*.txt'))):
    soubor=open("/home/mjakub/Desktop/asd/fabric8-analytics-worker.coverage."+str(i)+".txt","r")
    for cus in soubor:
        words = cus.split(" ")
        print(words)



