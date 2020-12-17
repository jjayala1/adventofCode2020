import itertools

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
    diff = [[],[]]

    print(new)

    for j in range(2,4):
        for i in range(len(new)-j):
            diff1 = []
            #print(j,i,new[i],new[i+j])

            if new[i+j] - new[i] <= 3:
                for jj in range(j-1):
                    diff1.append(new[i+jj+1])

            if len(diff1)>0:
                diff[j-2].append(diff1)
        #diff.append(sorted(list(set(diff1))))
    print(diff)
    print(len(diff[0]))
    print(len(diff[1]))

    print(diff)
    print(new)
    result = combination(diff[0])
    result = combination(diff[1])

    print(result);
    return result

def combination(diff):
    combs = 0
    n = len(diff)
    tot = 0

    #diff1 = diff[:]
    #for i in range(len(diff)-2):
    #    if diff[i+2] - diff[i+1] ==1 and diff[i+1] - diff[i] == 1:
    #        diff1.remove(diff[i])

    for i in range(len(diff)):
        combs1 = int(factorial(n) / (factorial(n-i) * factorial(i)))
        combs += combs1
        print(f'Getting combinations of {i} elements of {n} = {combs}')

    #n = len(diff1)
    #for i in range(3,n+1):
    #    combs1 = int(factorial(n) / (factorial(n-i) * factorial(i)))
    #    combs += combs1
    #    print(f'Getting combinations of {i} elements of {n} = {combs}')

    print(diff)
    #print(diff1)

    #print(f'Combinations = {combs} ')
    print(tot)
    return combs

def combination1(diff):
    combs = 0
    res = []
    n = len(diff)
    for i in range(1,n+1):
        #combs1 = int(factorial(n) / (factorial(n-i) * factorial(i)))
        #combs += combs1
        combs1 = list(itertools.combinations(diff,i))
        combs.append(res1)
        print(f'Getting combinations of {i} elements of {n} = {combs1} = {res}')
    print(f'Combinations = {combs} -- {res} ')
    print(len(res[2]))
    return combs


def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    #print(f'Factorial of {n} = {fact}')
    return fact




data = clean_data()
result = sort_adapters(data)
print(f'Part 1: {result}')
arrangements = count_arrangements(data)
print(f'Part 2: {arrangements}')
