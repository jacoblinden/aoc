from os import environ


def getSolutionPart2(input_list):
    aim = 0
    horizontal = 0
    depth = 0
    for command in input_list:
        if "forward" in command:
            horizontal += int(command[7:])
            depth += aim*int(command[7:])
        if "down" in command:
            aim += int(command[5:])
        if "up" in command:
            aim -= int(command[3:])
    return horizontal * depth


def getSolutionPart1(input_list):
    forward = 0
    depth = 0
    for command in input_list:
        if "forward" in command:
            forward += int(command[7:])
        if "down" in command:
            depth += int(command[5:])
        if "up" in command:
            depth -= int(command[3:])
    return forward*depth


with open('input.txt') as f:
    file_input = f.readlines()

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
