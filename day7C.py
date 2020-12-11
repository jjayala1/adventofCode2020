def get_data():

    data1 = []
    f = open('day7.txt','r')
    data =f.readlines()

    for d in data:

        for r in (('\n',''),('bags',''),('bag',''),('.','')):
            d = d.replace(*r)

        bags = d.split('contain')
        parent = bags[0].strip().replace(' ','_')
        childs = bags[1].strip().split(',')

        childs1 = []
        for c in childs:
            cc = c.split()
            childs1.append('0:no_other' if cc[0] == 'no' else f'{cc[0]}:{cc[1]}_{cc[2]}')
        data1.append(list([parent,childs1]))
    f.close()
    return data1



finded1 = []
def find_bags(bags):

    global data
    finded = []

    for d in data:
        for bag in bags:
            for dd in d[1]:
                if bag == dd.split(':')[1]:
                    finded.append(d[0])
                    finded1.append(d[0])
    if len(finded)>0:
       find_bags(finded)
    return finded1


def search_childs(search_bag, num_bags = 1):
    global data, acum

    for rule in data:
        if f'{search_bag}' in rule[0]:
            for child in rule[1]:
                child_cant, child_bag = child.split(':')
                mult = int(num_bags) * int(child_cant)
                acum += mult
                #print(d,mult,acum)
                search_childs(child_bag,mult)
    return True


acum = 0
data = get_data()
tot_bags = len(set(find_bags(['shiny_gold'])))
print(f'Part 1: {tot_bags}')
exit()
search_childs('shiny_gold')
print(f'Part 2: {acum}')
