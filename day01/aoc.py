from os import environ


def is_prime_number(number):
    is_prime = True
    if number > 1:
        for divisible in range(2, number):
            if number % divisible == 0:
                is_prime = False
                break
    return is_prime


def getSolutionPart1(input_list):
    index = 0
    tot = 0
    for num in input_list:
        tot += index * (num * is_prime_number(num))
        index += 1
    return tot


def multiplier(index):
    multi = -1
    if index % 2 == 0:
        multi = 1
    return multi


def getSolutionPart2(input_list):
    index = 0
    tot = 0
    for num in input_list:
        if not is_prime_number(num):
            tot += num * multiplier(index)
        index += 1
    return tot


with open('input.txt') as f:
    file_input = [int(x) for x in f.readlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
