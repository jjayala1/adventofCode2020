f = open('day2.txt','r')
i=1

for line in f:
    minmax, letter, password = line.split()
    min,max = minmax.split('-')
    letter = letter.split(':')[0]

    if letter in password:
        if int(min) <= password.count(letter) <= int(max):
            print(f'{i} -- {min} -- {max} --- {letter} --- {password}' )
            i+=1

f.close()


