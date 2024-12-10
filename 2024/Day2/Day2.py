# Day 2 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
import re;


# Part 1 list distance:
# Calculate whether each level is "safe"
# The rules:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def generateLists():
    inputFile = open("input");
    inputText = inputFile.read();
    levelsList = inputText.split("\n");
    levelsList = [level.split(" ") for level in levelsList];
    return levelsList;


# Checks whether the level is safe
def checkSafety(level):
    if len(level) > 1:
        direction = int(level[0]) - int(level[1]);
    else:
        return True;

    for i in range(1, len(level)):
        difference = int(level[i - 1]) - int(level[i]);

        if difference > 3 or difference == 0 or difference < -3:
            return False;
        if not difference * direction > 0:
            return False;

    return True;


levelsList = generateLists();
safetyList = []

for level in levelsList:
    safe = checkSafety(level);
    if safe:
        safetyList.append("Safe");
    else:
        safetyList.append("Unsafe");

print("Safe cases: ", safetyList.count("Safe"));
