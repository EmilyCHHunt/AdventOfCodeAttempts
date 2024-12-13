# Day 6 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
#
directions = ["up", "right", "down", "left"];


def readFile():
    # inputFile = open("testInput");
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText


def formatMap(mapString):
    map = mapString.split("\n")
    for i in (range(len(map))):
        map[i] = list(map[i]);
    return map;


def findStart(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                guardPos = [i, j];
                return guardPos;
    return -1;


def simulate(map):
    facing = 0;
    outOfMap = False;
    guardPos = findStart(map);
    if guardPos == -1:
        return False;
    updateMap(guardPos, map)
    while not outOfMap:
        guardPos, facing = moveGuard(guardPos, facing, map);

        if guardPos == [-10, -10]:
            outOfMap = True;
    countTheMoves(map);
    return map;


def moveGuard(guardPos, facing, map):
    newGuard = guardPos.copy();
    match directions[facing]:
        case "up":
            newGuard[0] += -1;
            if not checkBounds(newGuard):
                if map[guardPos[0] - 1][ guardPos[1]] == '#':
                    facing = 1;
                    return guardPos, facing;
            guardPos[0] -= 1;
        case "down":
            newGuard[0] += 1;
            if not checkBounds(newGuard):
                if map[guardPos[0] + 1][ (guardPos[1])] == "#":
                    facing = 3;
                    return guardPos, facing;
            guardPos[0] += 1
        case "left":
            newGuard[1] += -1
            if not checkBounds(newGuard):
                if map[(guardPos[0])][ guardPos[1] - 1] == "#":
                    facing = 0;
                    return guardPos, facing;
            guardPos[1] += -1
        case "right":
            newGuard[1] += 1
            if not checkBounds(newGuard):
                if map[(guardPos[0])][ guardPos[1] + 1] == "#":
                    facing = 2;
                    return guardPos, facing;
            guardPos[1] += 1
    if checkBounds(guardPos):
        return [-10, -10], -2;
    updateMap(guardPos, map);
    return guardPos, facing;


def checkBounds(coords):
    x = coords[0];
    y = coords[1];
    if x < 0 or y < 0 or x >= len(map[y]) or y >= len(map):
        return True;
    return False;


def updateMap(guardPos, map):
    x = guardPos[1];
    y = guardPos[0];
    map[y][x] = "X";

def printMap(map):
    for line in map:
        print(line);

def countTheMoves(map):
    total = 0;
    for line in map:
        for space in line:
            if space == "X":
                total += 1;
    print("Total moves: ", total);

if __name__ == '__main__':
    map = formatMap(readFile());
    printMap(simulate(map));
