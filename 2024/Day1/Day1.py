# Day 1 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
import re;

# Part 1 list distance:
# Calculate the distance between the two lists
def generateLists():
    inputFile = open("input");
    inputText = inputFile.read();
    inputList = re.split("\n|   ",inputText);

    locIDList1 = inputList[::2]
    locIDList2 = inputList[1::2]
    return locIDList1, locIDList2;

locIDList1, locIDList2 = generateLists();
totalDistance = 0
locIDList1.sort();
locIDList2.sort();
distanceList = [abs(int(locIDList1[i]) - int(locIDList2[i])) for i in range(len(locIDList1))];
distance = sum(distanceList)
print("distance : ", distance);

# Part 2
# Find the similarity of the list:
# Multiply every number in list 1 by the number of times it occurs
list1, list2 = generateLists();
similarity = 0;
similarityList = [int(index) * list2.count(index) for index in list1];
similarity = sum(similarityList);
print("similarity : ", similarity);