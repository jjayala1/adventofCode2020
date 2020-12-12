def clean_data():

    f = open('day9.txt','r')
    data = [x.replace('\n','') for x in f.readlines()]
    return data


def find_error(data):

    for i in range(25,len(data)):

        search = int(data[i])
        preamble = data[i-25:i]

        valid = False

        for a,b in [(int(a),int(b)) for a in preamble for b in preamble]:
            #print(f'{a}+{b}={a+b} {search}')

            if a+b == search:
                valid = True
                break

        if valid == False:
            #print(f'{i} {search} {a}+{b}={a+b} --  {valid}')
            return search


def find_weakness(data, error, depth = 2):

    is_valid = False

    for i in range(len(data)-depth+1):

        weakness_range = []
        check = 0

        for dep in range(depth):
            check += int(data[i+dep])
            weakness_range.append(int(data[i+dep]))

        if int(check) == int(error):
            is_valid = True
            break

    if not is_valid:
        depth += 1
        return find_weakness(data, error, depth)
    else:
        weakness_range.sort()
        return weakness_range[0] + weakness_range[len(weakness_range)-1]


data = clean_data()
error = find_error(data)
print(f'Part 1: {error}')
weakness = find_weakness(data, error)
print(f'Part 2: {weakness}')
