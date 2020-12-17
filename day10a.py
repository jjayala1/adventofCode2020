def clean_data():

    f = open('day10b.txt','r')
    data = [int(x.replace('\n','')) for x in f.readlines()]
    data.sort()
    return data


def sort_adapters(data):

    dif1 = 1
    dif3 = 1

    for i in range(len(data)-1):

        dif = data[i+1] - data[i]
        #print(f'{i} -- {data[i+1]} - {data[i]} -- {data[i+1] - data[i]} -- {dif1} -- {dif3}')

        if dif == 1:
            dif1 += 1

        elif dif == 3:
            dif3 += 1

    return dif1*dif3


def count_arrangements(data):

    new = [0]
    new += data[:]
    new.append(new[len(new)-1] + 3)
    path1 = []

    for i in range(len(new)-1):
        path1.append(0)
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

    new = [0]
    new += data[:]
    new.append(new[len(new)-1] + 3)

    path1 = []
    path1.append(1)

    for i in range(len(new)):

        path1.append(0)
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
