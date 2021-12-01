import sys
from os import environ


def getSolutionPart2(input_list):
    return


def getSolutionPart1(input_list):
    previous = sys.maxsize
    count = 0
    for depth in input_list:
        if depth > previous:
            count += 1
        previous = depth
    return count


with open('input.txt') as f:
    file_input = [int(x) for x in f.readlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
