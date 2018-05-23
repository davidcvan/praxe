import matplotlib.pyplot as plt
lines = []
with open("/home/tkrejzlik/Desktop/data/praxe-master/data/praxe-master/data/praxe-master/data/fabric8-analytics-worker.coverage.0.txt","r") as f:
    for line in f:
        words = line.split()
        lines.append(words)
del lines[0]
del lines[0]
del lines[-1]
del lines[-1]
for i in range(len(lines)):
    loc = int(lines[i][1])
    tested_loc = int(lines[i][2])
    plt.title(lines[i][0])
    plt.plot([1],[loc],'ro',label = "loc")
    plt.plot([1],[tested_loc],'bs',label = "tested_loc")
    plt.legend()
    plt.show()
print(lines),loc,loc