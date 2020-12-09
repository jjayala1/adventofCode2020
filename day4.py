import json
import re

def cleanPassport():

    passports = []

    f = open('day4.txt','r')

    data =f.readlines()
    passport = ''

    for d in data:
        d = d[0:len(d)-1]
        passport += ' ' + d

        if d == '':
            passports.append(passport)
            #print(f'{d} {passport}')
            passport = ''
    return passports

def validatePassport(passports):
    valid_tags = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0
    valid2 = 0

    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    #cid (Country ID) - ignored, missing or not.

    for p in passports:
        check = 0

        for t in valid_tags:
            if t in p:
                check += 1
        if check == 7:
            valid += 1
            valid2 += validateData(p)
    return valid2



def validateData(passport):

    data = passport.split()
    data.sort();

    valid_data = {
                  0:{'tag': 'byr', 'regex': '(^19[2-9][0-9]$|^200[0-2]$)'},
                  1:{'tag': 'iyr', 'regex': '^20([1][0-9]$|20$)'},
                  2:{'tag': 'eyr', 'regex': '^20([2][0-9]$|30$)'},
                  3:{'tag': 'hgt', 'mincm': 150, 'minin': 59, 'maxcm': 1193, 'maxin': '76'},
                  4:{'tag': 'hcl', 'regex': '^#([0-9]|[a-z]){6}$'},
                  5:{'tag': 'ecl', 'regex': '^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$'},
                  6:{'tag': 'pid', 'regex': '^[0-9]{9}$'},
                 }

    tag_validated = 0
    tags_validated = 0
    num_tags = 7
    num_tags1 = 0
    cant_tags=num_tags-num_tags1

    for d in data:
        for i in range(0,7):
            if valid_data[i]['tag'] in d:
                value = d.split(':')
                value = value[1].strip()

                if valid_data[i]['tag'] != 'hgt':
                    regex = re.compile(rf'{valid_data[i]["regex"]}')
                    if(regex.search(value)):
                        tag_validated += 1

                else:
                    if 'cm' in value:
                        valid_data[i]['min'] = valid_data[i]['mincm']
                        valid_data[i]['max'] = valid_data[i]['maxcm']
                        value = value[0:len(value)-2]

                    elif 'in' in value:
                        valid_data[i]['min'] = valid_data[i]['minin']
                        valid_data[i]['max'] = valid_data[i]['maxin']
                        value = value[0:len(value)-2]

                    else:
                        valid_data[i]['min'] = 0
                        valid_data[i]['max'] = 0

                    if int(valid_data[i]['min']) <= int(value) <= int(valid_data[i]['max']):
                        tag_validated += 1

                if tag_validated == cant_tags:
                    tags_validated = 1
                else:
                    tags_validated = 0

                #print(f'{valid_data[i]["tag"]} -- {value} -- {tag_validated} -- {tags_validated} --', end='#')

    return tags_validated


one_line_passports = cleanPassport()
valid_passports = validatePassport(one_line_passports)
print(valid_passports)

