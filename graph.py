import matplotlib.pyplot as plt

def opening(name, date):
    with open(name,"r") as f:
        lines.append([date])
        for line in f:
            if line[0] == "s":
                words = line.split()
                lines.append(words)



def draw_graph(file_name):
    contr=False
    x_axis = []
    loc = []
    tested_loc = []
    for i in range(len(lines)):
        if len(lines[i])==1:
            name = lines[i][0]
        elif lines[i][0] == file_name:
            x_axis.append(name)
            loc.append(int(lines[i][1]))
            tested_loc.append(int(lines[i][1]) - int(lines[i][2]))

    for i in range(len(cs)):
        if file_name==cs[i]:
            contr = True
    print(cs)
    if contr != True:
        cs.append(file_name)
        plt.title(file_name)
        if len(x_axis) == 1:
            plt.plot(x_axis, loc,"ro", label="loc")
            plt.plot(x_axis, tested_loc,"ro", label="tested_loc")
        else:
            plt.plot(x_axis, loc, label = "loc")
            plt.plot(x_axis,tested_loc, label = "tested_loc")

        plt.xticks(size=7)
        plt.yticks(size=10)
        plt.xticks(x_axis, rotation='vertical')
        #plt.savefig(file_name.replace("/", "_") + ".png")
        plt.legend()
        plt.show()

cs = []
lines = []
'''
files = ["./data/fabric8-analytics-worker.coverage.0.txt","./data/fabric8-analytics-worker.coverage.1.txt","./data/fabric8-analytics-worker.coverage.2.txt","./data/fabric8-analytics-worker.coverage.3.txt"]
for file in files:
    opening(file)

for file in lines:
    if len(file) > 1:
        draw_graph(file[0])
'''