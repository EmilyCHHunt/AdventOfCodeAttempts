# Day 2 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt

# Task2 the reports are now safe if by removing a level it is safe
def generateLists():
    inputFile = open("input");
    inputText = inputFile.read();
    reportsList = inputText.split("\n");
    reportsList = [level.split(" ") for level in reportsList];
    return reportsList;

# Checks whether the level is safe
def checkSafety(level, failedBefore):
    if len(level) > 1:
        direction = int(level[0]) - int(level[1]);
    else:
        return True;

    for i in range(1,len(level)):
        difference = int(level[i-1]) - int(level[i]);

        if difference > 3 or difference == 0 or difference < -3:
            if not failedBefore:
                for j in range(len(level)):
                    newLevel = level.copy();
                    del newLevel[j];
                    if checkSafety(newLevel, True):
                        return True;
            return False;

        if not difference * direction > 0:
            if not failedBefore:
                for j in range(len(level)):
                    newLevel = level.copy();
                    del newLevel[j];
                    if checkSafety(newLevel, True):
                        return True;
            return False;

    return True;

levelsList = generateLists();
safetyList = []

for level in levelsList:
    safe = checkSafety(level, False);
    if safe:
        safetyList.append("Safe");
    else:
        safetyList.append("Unsafe");

print("Safe cases: ", safetyList.count("Safe"));
