from os import environ


def create_matrix(commands):
    max_x = -1
    max_y = -1
    for command in commands:
        split_command = command.split(',')
        max_x = max(int(split_command[0]), max_x)
        max_y = max(int(split_command[1]), max_y)
    line = []
    row = []
    for x in range(max_x + 1):
        line.append(1)
    for y in range(max_y + 1):
        row.append(line.copy())
    return row


def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


def fold(fold_command, matrix):
    commandNumber = int(fold_command[fold_command.find("=") + 1:])
    if "x" in fold_command:
        matrix = rotate_matrix(matrix)

    part1 = matrix[0:commandNumber]
    part1.reverse()
    part2 = matrix[commandNumber + 1:]
    matrix = multiplyMatrix(part1, part2)

    if "x" in fold_command:
        matrix = rotate_matrix(matrix)

    return matrix


def multiplyMatrix(X, Y):
    indexRow = -1
    result = []
    for row in X:
        indexRow += 1
        newLine = []
        for line in range(len(row)):
            nx= X[indexRow][line]
            ny = Y[indexRow][line]
            newLine.append(ny*nx)
        result.append(newLine)
    return result


def execute_commands(commands, foldCommands):
    matrix = create_matrix(commands)
    for command in command1:
        split_command = command.split(",")
        matrix[int(split_command[1])][int(split_command[0])] = 2
    for foldcommand in foldCommands:
        matrix = fold(foldcommand, matrix)
        matrix.reverse()
    return matrix


def getSolutionPart1(commands, foldCommands):
    matrix = execute_commands(commands, [foldCommands[0]])
    return count(matrix)


def getSolutionPart2(commands, foldCommands):
    matrix = execute_commands(commands, foldCommands)
    return letter(matrix)

def letter(matrix):
    counter = 0
    for row in matrix:
        counter += 1
        for obj in row:
            if obj > 1:
                obj = "#"
            else:
                obj = "."
            print(obj,"",end = '')
        print()
    return matrix

def count(matrix):
    counter = 0
    for row in matrix:
        for obj in row:
            if obj > 1:
                counter += 1
    return counter

with open('input.txt') as f:
    file_input = f.readlines()
    command1 = [command for command in file_input if "," in command]
    command2 = [command for command in file_input if "fold" in command]

print('Python')
part = environ.get('part')

if part == 'part2':
    print("part2")
else:
    print(getSolutionPart1(command1,command2 ))
    print(getSolutionPart2(command1,command2))
