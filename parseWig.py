def parseWig(filename):
    with open filename as f:
        content = [line.rstrip for line in f.readlines()]
    del content[0]
    del content[1] #strip headers

    position = []
    value = []

    for row in content:
        #split by the tab sep.
        position.append(row.split('\t')[0])
        value.append(row.split('\t')[1])

    wigDict = dict(zip(position,value))

    return wigDict
