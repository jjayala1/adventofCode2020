
def getTrees(h,v):

    f = open('day3.txt','r');
    data=f.readlines()
    j = 0
    i = 0
    trees = 0
    mult = 0
    hor,vert = h,v

    for l in data:

        if(j % vert == 0):
            l = l[0:len(l)-1]

            if i >= len(l):
                mult = (i//len(l)+1)
                l = l * mult

            if l[i] == '#':
                trees += 1

            #print(f'{j} -- {i} -- {mult} -- {l} -- {l[i]} -- {trees}')
            i += hor
        j += 1

    #print(f'Hubo {trees} arboles')
    return(trees)


#Part 1
r1 = getTrees(3,1)
print(f'Part 1: There were {r1} trees')

#Part 2
r1 = getTrees(1,1)
r2 = getTrees(3,1)
r3 = getTrees(5,1)
r4 = getTrees(7,1)
r5 = getTrees(1,2)

print(f'Part 2: The final result is { r1 * r2 * r3 * r4 * r5}')

