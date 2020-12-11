def get_data():

    data1 = []
    f = open('day7.txt','r')
    data =f.readlines()

    for d in data:
        d = d[0:len(d)-1]
        d = d.replace('bags','')
        d = d.replace('bag','')
        d = d.replace('.','')

        bags = d.split('contain')
        parent = bags[0].strip().replace(' ','_')
        childs = bags[1].strip().split(',')
        #childs = dict(map(lambda x,y: x.strip(), childsi,split()))
        #childs = [(c.split()) for (c) in childs]

        childs1 = []
        for c in childs:
            cc = c.split()

            if cc[0] == 'no':
                child = '0:no_other'
            else:
                child = f'{cc[0]}:{cc[1]}_{cc[2]}'
            childs1.append(child)
        data1.append(list([parent,childs1]))
        #break
    f.close()
    return data1



def search_childs(search_bag, num_bags = 1):

    global data, acum, level, cuenta

    if search_bag == 'no_other':
        print('ok')
        level -= 1
        #return 1

    for d in data:

        if f'{search_bag}' in d[0]:

            if len(d[1]) > 1:
                level +=1

            for ch in d[1]:
                ch_data = ch.split(':')
                ch_cant = ch_data[0]
                ch_bag = ch_data[1]
                mult = int(num_bags) * int(ch_cant)
                cuenta.append(mult)
                acum += mult
                print(d,mult,acum,level)
                search_childs(ch_bag,mult)
            #print(c[1])
            #print(search_bag,d)
    print('------------------')


acum = 0
level = 0
cuenta = []
data = get_data()
#for i,d in enumerate(data):
#    print(i,d)
#exit()
#check_parents(data)
search_childs('shiny_gold')
print(acum)
#search_childs('wavy_chartreuse')
#search_childs('dim_chartreuse')
