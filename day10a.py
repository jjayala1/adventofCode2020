def clean_data():

    f = open('day10.txt','r')
    data = sorted([int(x.replace('\n','')) for x in f.readlines()])
    data = [0, *data, data[-1] + 3 ]
    return data

def sort_adapters(data):
    dif = [(data[i+1]-data[i]) for i in range(len(data)-1) ]
    return  dif.count(1) * dif.count(3)


def count_arrangements(data):

    new = data[:]
    path1 = [0 for x in range(len(new)-1)]
    path1.append(1)

    for i in range(len(new)-1,-1,-1):

        paths = 0
        for j in range(1,4):
            if i+j < len(new) and new[i+j] - new[i] <= 3:
                paths += 1
                path1[i] += path1[i+j]
        #print(f'Connector: {new[i]} -- Iteration: {i} -- Paths: {paths} -- TotPaths: {path1[i]} ')
    return path1[0]


def count_arrangements1(data):

    new = data[:]
    path1 = [0 for x in range(1,len(new))]
    path1.insert(0,1)

    for i in range(len(new)):

        paths = 0
        for j in range(1,4):
            if i-j >= 0 and new[i] - new[i-j] <= 3:
                paths += 1
                path1[i] += path1[i-j]
        #print(f'Connector: {new[i]} -- Iteration: {i} -- Paths: {paths} -- TotPaths: {path1[i]}  ')
    return path1[len(path1)-2]

data = clean_data()
result = sort_adapters(data)
print(f'Part 1: {result}')
arrangements = count_arrangements(data)
print(f'Part 2a descending: {arrangements}')
arrangements1 = count_arrangements1(data)
print(f'Part 2b ascending : {arrangements1}')
