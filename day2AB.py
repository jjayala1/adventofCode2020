#Part 1
f = open('day2.txt','r')
i=0

for line in f:
    minmax, letter, password = line.split()
    min,max = minmax.split('-')
    letter = letter.split(':')[0]

    if letter in password:
        if int(min) <= password.count(letter) <= int(max):
            i+=1
            #print(f'{i} -- {min} -- {max} --- {letter} --- {password}' )

print(f'Valid passwords {i}')
f.close()


#Part 2
f = open('day2.txt','r')
i=0

for line in f:
    minmax, letter, password = line.split()
    min,max = minmax.split('-')
    min = int(min)
    max = int(max)
    letter = letter.split(':')[0]

    if letter in password:
        if (password[min-1] == letter and password[max-1] != letter) or (password[min-1] != letter and password[max-1] == letter):
            i+=1
            #print(f'{i} -- {min} -- {max} --- {letter} --- {password}' )

print(f'Valid passwords {i}')
f.close()


