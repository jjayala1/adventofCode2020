

def clean_groups():

    groups = []

    f = open('day6.txt','r')

    data =f.readlines()
    group = ''

    for d in data:
        d = d[0:len(d)-1]
        group += ' ' + d

        if d == '':
            groups.append(group)
            group = ''
    return groups


def count_uinique_answers_part1(groups):
    total_count = 0

    for g in groups:
        g = g.replace(' ','')
        answers = list(g)
        answers.sort()
        answers = set(answers)
        total_count += len(answers)
    return total_count


def count_uinique_answers_part2(groups):
    total_count = 0

    for g in groups:
        answers = g.split()
        total_count += find_duplicates(answers)
        #print(answers, total_count)
    return total_count


def find_duplicates(group):

    if len(group) == 1:
        return len(list(group[0]))

    intersect = group[0]

    for i,d in enumerate(group):

        intersect = set(group[i]).intersection(intersect)
        #print(intersect)
    return len(intersect)



groups = clean_groups()
total1 = count_uinique_answers_part1(groups)
total2 = count_uinique_answers_part2(groups)
print(f'Part 1: {total1}')
print(f'Part 2: {total2}')
