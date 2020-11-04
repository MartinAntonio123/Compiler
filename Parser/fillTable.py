import sys

def fillAction(table):
    d = {}
    arr = []
    file = open(table, 'r')
    Lines = file.readlines()
    mystate = 1
    keys = []
    vals = []
    for line in Lines:
        line = line.strip()
        line = str(line)
        if mystate == 1:
            keys = line.split(",")
            mystate = 2
        elif mystate == 2:
            x = line.split(",")
            for value in x:
                vals.append([value])
            mystate = 3
        elif mystate == 3:
            x = line.split(",")
            for i in range(len(x)):
                vals[i].append(x[i])
    for i in range(len(keys)):
        d[keys[i]] = vals[i]
    print(d['id'])



print(fillAction(sys.argv[1]))
