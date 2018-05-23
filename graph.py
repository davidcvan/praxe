import matplotlib.pyplot as plt
lines = []
dict = {}

def opening(name):
    with open(name,"r") as f:
        lines.append([name])
        for line in f:
            if line[0] == "/":
                words = line.split()
                lines.append(words)

def draw_graph(file_name):
    x_axis = []
    loc = []
    tested_loc = []
    for i in range(len(lines)):
        if len(lines[i])==1:
            x_axis.append(lines[i][0])
        elif lines[i][0] == file_name:
            loc.append(int(lines[i][1]))
            tested_loc.append(int(lines[i][2]))
    print(x_axis, loc, tested_loc)
    plt.title(file_name)
    plt.plot(x_axis, loc, label = "loc")
    plt.plot(x_axis,tested_loc, label = "tested_loc")
    plt.legend()
    plt.show()

opening("./data/fabric8-analytics-worker.coverage.0.txt" )
opening("./data/fabric8-analytics-worker.coverage.1.txt" )
draw_graph("/f8a_worker/f8a_worker/base.py")
