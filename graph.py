import numpy as np
import matplotlib.pyplot as plt
lines = []
with open("./data/fabric8-analytics-worker.coverage.0.txt") as f:
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
    plt.plot([1,2,3],[loc,loc,loc])
    plt.plot([1,2,3],[tested_loc,tested_loc,tested_loc])
    plt.show()
print(lines)

