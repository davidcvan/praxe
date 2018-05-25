import os

lines = []
os.system("cd ./fabric8-analytics.github.io; git log --pretty=oneline > logs.txt")
with open("./fabric8-analytics.github.io/logs.txt","r") as f:
    for line in f:
        splitted_line = line.split()
        if splitted_line[1] == "Dashboard" and len(splitted_line) <= 3:
            lines.append(splitted_line)
    f.close()
print(lines, len(lines))