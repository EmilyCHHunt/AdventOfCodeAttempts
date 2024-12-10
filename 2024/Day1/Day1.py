# Day 1 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
import re;

# Part 1 list distance:
# Shorthand explanation: calculate the distance between the two lists
# We have been given two lists in the input file they are then separated and sorted.
# Each item in the second list is subtracted from the first and the absolute result is added to a total
# to calculate the distance between the lists
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
# Shorthand explanation:
# Multiply every number in list 1 by the number of times it occurs in list 2
# so if the number 3 appears in list two 4 times we calculate 3*4 and add it to the similarity value
list1, list2 = generateLists();
similarity = 0;
similarityList = [int(index) * list2.count(index) for index in list1];
similarity = sum(similarityList);
print("similarity : ", similarity);