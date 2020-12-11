def clean_data():

    f = open('day8.txt','r')
    data = f.readlines()

    for i,d in enumerate(data):
        for r in (('\n',''),('bags',''),('bag',''),('.','')):
            d = d.replace(*r)
            data[i] = d
    return data


def get_acum(data):

    acum = 0
    loop = []
    j = 0

    for i,d in enumerate(data):
        op, value = data[j].split()

        loop.append(j)
        acum += int(value) if op == 'acc' else 0
        j += int(value) if op == 'jmp' else 1

        if j in loop:
            return acum,j
        if j == len(data):
            return acum,j
    return acum,j



changed = []

def change_op(data):

    global changed

    datan = data.copy()
    change = 0

    for i,d in enumerate(data):
        op, value = d.split()

        if op == 'jmp' and change == 0 and i not in changed:
            datan[i] = 'nop ' + value
            changed.append(i)
            change = 1
            #print(f'changing {i}')

        if op == 'nop' and change == 0 and i not in changed:
            datan[i] = 'jmp ' + value
            changed.append(i)
            change = 1

    if change == 0:
        exit()

    acum,j = get_acum(datan)

    if j != len(data):
        return change_op(data)
    else:
        return(acum,j)

data = clean_data()
acum = get_acum(data)
acum2 = change_op(data)
print(f'Part 1: {acum[0]}')
print(f'Part 2: {acum2[0]}')
