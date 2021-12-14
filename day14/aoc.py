from os import environ


def getSolutionPart1(commands, foldCommands):
    return


def getSolutionPart2(commands, foldCommands):
    return

def count(matrix):
    return 1


with open('input.txt') as f:
    file_input = f.readlines()
    command1 = [command for command in file_input if "->" in command]
    command2 = [command for command in file_input if "'" in command]

print('Python')
part = environ.get('part')

if part == 'part2':
    print("part2")
else:
    print(getSolutionPart1(command1,command2 ))
    print(getSolutionPart2(command1,command2))
