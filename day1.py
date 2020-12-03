f = open('day1.txt','r');
data = f.readlines()
data2 = data[1:]
f.close()
t = 0

for a,b in [(a,b) for a in data for b in data2]:
    t += 1
    if int(a)+int(b) == 2020:
        print(int(a)*int(b))
        break

print(t)
