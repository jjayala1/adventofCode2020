#Part 1
f = open('day1.txt','r');
data = f.readlines()
data2 = data[1:]
f.close()

for a,b in [(a,b) for a in data for b in data2]:
    if int(a)+int(b) == 2020:
        print(int(a)*int(b))
        break


#Part 2
f = open('day1.txt','r');
data = f.readlines()
f.close()

for a,b,c in [(a,b,c) for a in data for b in data for c in data]:
    if int(a)+int(b)+int(c) == 2020:
        print(int(a)*int(b)*int(c))
        break
