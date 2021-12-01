from os import environ


def getSolutionPart2(input_list):
    previous = -1
    count = 0
    for i in range(0, len(input_list)-2):
        depth = input_list[i] + input_list[i+1] + input_list[i+2]
        count += add(previous, depth)
        previous = depth
    return count


def getSolutionPart1(input_list):
    previous = input_list[0]
    count = 0
    for i in range(1, len(input_list)):
        depth = input_list[i]
        count += add(previous, depth)
        previous = depth
    return count


def add(previous, next):
    if next > previous & previous != -1:
        return 1
    return 0


with open('input.txt') as f:
    file_input = [int(x) for x in f.readlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
