import os
import graph
commits = []
file = "fabric8-analytics.github.io/dashboard/f8a-server-backbone.coverage.txt"

def opening():
    os.system("cd fabric8-analytics.github.io; git log --pretty=oneline > logs.txt")

    with open("./fabric8-analytics.github.io/logs.txt","r") as f:
        for line in f:
            splitted_line = line.split()
            if splitted_line[1] == "Dashboard" and len(splitted_line) == 3:
                commits.append(splitted_line)
        commits.reverse()
        f.close()
    print(commits, len(commits))

def checkout():
    for commit in commits:
        os.system("cd ./fabric8-analytics.github.io; git checkout %s" % (commit[0]))
        print(os.path.exists(file))
        if os.path.exists(file):
            graph.opening(file, commit[2])


opening()
checkout()
for file in graph.lines:
    if len(file) > 1:
        graph.draw_graph(file[0])

