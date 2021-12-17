from os import environ

from day14.node import Graph


def getSolutionPart1(input_list):
    adjac_lis = formatValues(input_list)
    graph1 = Graph(adjac_lis, len(input_list), len(input_list[0]))
    txt = "r: {index:.0f} n: {node:.0f}"
    start = txt.format(index=0, node=0)
    end = txt.format(index=len(input_list)-1, node=len(input_list[0])-2)
    lastLine = input_list[len(input_list)-1]
    lastCost = int(lastLine[len(lastLine)-1])
    path = graph1.a_star_algorithm(start, end,lastCost)
    cost  = path[1]
    return cost


def formatValues(input_list):
    paths_between_nodes = {}
    input_list = list(map(lambda s: s.strip(), input_list))
    for index in range(0, len(input_list)):
        line = input_list[index]
        maxRightcordinat = len(line)-1
        prevN = -1
        for node in range(0, len(line)):
            txt = "r: {index:.0f} n: {node:.0f}"
            rNode = [txt.format(index=index, node=node + 1), int(line[node + 1])] if maxRightcordinat > node  else None
            lNode = [txt.format(index=index, node=node - 1), int(line[node - 1])] if prevN > -1 else None
            dNode = [txt.format(index=index+1, node=node), int(input_list[index + 1][node])] if index + 1 < len(
                input_list) else None
            uNode = [txt.format(index=index-1, node=node), int(input_list[index - 1][node])] if index > 0 else None
            nodesToAdd = list(filter(None, [lNode, dNode, rNode, uNode]))
            paths_between_nodes[txt.format(index=index, node=node)] = nodesToAdd
            prevN = node
    return paths_between_nodes




def getSolutionPart2(commands, foldCommands):
    return


def count(matrix):
    return 1


with open('input.txt') as f:
    file_input = f.readlines()
print('Python')
part = environ.get('part')

if part == 'part2':
    print("part2")
else:
    print(getSolutionPart1(file_input))
