from os import environ


def getSolutionPart1(xMin,xMax,yMin,yMax):
    maxY = []
    for yVel in range(-100,100):
        path = maxCordBasedOnX(xMin,xMax,yMin,yMax,yVel)
        if path[0]:
            maxY.append(path[0])
    return max(maxY)


def maxCordBasedOnX(xMin, xMax, yMin, yMax, yVelocity):
    succeeded = []
    intitialVel = []
    for xVelocity in range(-500,500):
        cords = [0, 0]
        maxY = -999999999
        currentX = xVelocity
        currentY = yVelocity
        for time in range (0,100):
            cords[0] = cords[0] + currentX
            cords[1] = cords[1] + currentY
            maxY = cords[1] if cords[1] > maxY else maxY
            currentY = currentY - 1
            currentX = currentX - 1 if currentX > 0 else currentX
            if hasMissedTarget(xMin, xMax, yMin, yMax, cords, currentX, currentY):
                break
            if isWithinMissonArea(xMin, xMax, yMin, yMax, cords):
                succeeded.append(maxY)
                intitialVel.append({xVelocity,yVelocity})
                break
    return [max(succeeded) if len(succeeded) > 0 else None, intitialVel]


def isWithinMissonArea(xMin,xMax,yMin,yMax, currentPosition):
    return currentPosition[0] >= xMin and currentPosition[0] <= xMax and currentPosition[1] >= yMin and currentPosition[1] <= yMax


def hasMissedTarget(xMin,xMax,yMin,yMax, currentPosition,xV,yV):
    # has passed x
    if (currentPosition[0] > xMax and xV>=0): return True
    # has passed y
    elif(currentPosition[1] < yMin and yV<=0): return True

    else: return False


def getSolutionPart2(xMin, xMax, yMin, yMax):
    possiblePath = []
    for yVel in range(-100, 100):
        path = maxCordBasedOnX(xMin, xMax, yMin, yMax, yVel)
        if path[1]:
            possiblePath += path[1]
    return len(possiblePath)

with open('input.txt') as f:
    file_input = f.readlines()
    input = file_input[0].split(",")
print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(int(input[0]), int(input[1]), int(input[2]), int(input[3])))
else:
    print(getSolutionPart1(int(input[0]),int(input[1]),int(input[2]),int(input[3])))
