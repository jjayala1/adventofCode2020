f = open('day1.txt','r');
data = f.readlines()
f.close()
t = 0

for a,b,c in [(a,b,c) for a in data for b in data for c in data]:
    t += 1
    if int(a)+int(b)+int(c) == 2020:
        print(int(a)*int(b)*int(c))
        break

print(t)
