def clean_data():

    f = open('day10.txt','r')
    jolts = sorted([int(x.replace('\n','')) for x in f.readlines()])
    jolts = [0, *jolts, jolts[-1] + 3 ]
    return jolts

def sort_adapters(jolts):
    dif = [(jolts[i+1]-jolts[i]) for i in range(len(jolts)-1) ]
    return  dif.count(1) * dif.count(3)


def count_arrangements(jolts):

    paths = [0 for x in range(len(jolts)-1)]
    paths.append(1)

    for i in range(len(jolts)-1,-1,-1):
        for j in range(1,4):
            if i+j < len(jolts) and jolts[i+j] - jolts[i] <= 3:
                paths[i] += paths[i+j]
        #print(f'Connector: {jolts[i]} -- Iteration: {i} -- Paths: {paths} -- TotPaths: {paths[i]} ')
    return paths[0]


def count_arrangements1(jolts):

    paths = [0 for x in range(1,len(jolts))]
    paths.insert(0,1)

    for i in range(len(jolts)):
        for j in range(1,4):
            if i-j >= 0 and jolts[i] - jolts[i-j] <= 3:
                paths[i] += paths[i-j]
        #print(f'Connector: {jolts[i]} -- Iteration: {i} -- Paths: {paths} -- TotPaths: {paths[i]}  ')
    return paths[-1]

jolts = clean_data()
result = sort_adapters(jolts)
print(f'Part 1: {result}')
arrangements = count_arrangements(jolts)
print(f'Part 2a descending: {arrangements}')
arrangements1 = count_arrangements1(jolts)
print(f'Part 2b ascending : {arrangements1}')
