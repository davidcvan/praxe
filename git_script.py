import os

os.system("cd ./fabric8-analytics.github.io; git log --pretty=oneline > logs.txt")
with open("./fabric8-analytics.github.io/logs.txt","r") as f:
    for line in f:
        print(f.readline())