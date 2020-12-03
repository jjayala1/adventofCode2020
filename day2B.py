f = open('day2.txt','r')
i=1

for line in f:
    minmax, letter, password = line.split()
    min,max = minmax.split('-')
    min = int(min)
    max = int(max)
    letter = letter.split(':')[0]

    if letter in password:
        if (password[min-1] == letter and password[max-1] != letter) or (password[min-1] != letter and password[max-1] == letter):
            print(f'{i} -- {min} -- {max} --- {letter} --- {password}' )
            i+=1

f.close()


