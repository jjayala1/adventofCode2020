
def getRow(d, min = 0, max = 128):

    if d[0:1] == 'F':
        max = max - ((max - min) / 2)

    if d[0:1] == 'B':
        min = min + ((max - min) / 2)

    if min == max - 1:
        return(min)

    else:
        return getRow(d[1:], min, max)


def getCol(d, min = 0, max = 8):

    if d[0:1] == 'L':
        max = max - ((max - min) / 2)

    if d[0:1] == 'R':
        min = min + ((max - min) / 2)

    if min == max - 1:
        return(min)

    else:
        return getCol(d[1:], min, max)



f = open('day5.txt', 'r')
data = f.readlines()
ids = []

for d in data:
    d = d[0:len(d)-1]
    row = getRow(d[0:7])
    col = getCol(d[7:])
    id = row * 8 + col
    ids.append(id)
    #print(f'{row} - {col} - {id}')

ids.sort()
print(f'Part 1: {int(ids[len(ids)-1])}')

for i in range(8, len(ids) -9):

    if ids[i-8] != i:
        print(f'Part 2: {i}')
        break


