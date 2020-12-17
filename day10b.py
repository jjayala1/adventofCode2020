def clean_data():

    f = open('day10b.txt','r')
    data = [int(x.replace('\n','')) for x in f.readlines()]
    data.sort()
    return data

def part2(data):

    data.sort()
    print(data)

    ans = {}
    ans[0] = 1

    for a in data:
        ans[a] = ans.get(a-1,0) + ans.get(a-2,0) + ans.get(a-3,0)
        print(a,ans[a],ans.get(a-1,0),ans.get(a-2,0),ans.get(a-3,0))

    print(ans,ans[data[-1]])


data = clean_data()
result = part2(data)
print(f'Part 2: {result}')
