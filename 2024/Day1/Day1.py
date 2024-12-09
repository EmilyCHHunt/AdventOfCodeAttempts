# Day 1 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
import re;

# Part 1 list distance:
# Calculate the distance between the two lists
inputFile = open("input");
inputText = inputFile.read();
inputList = re.split("\n|   ",inputText);

locIDList1 = inputList[::2]
locIDList2 = inputList[1::2]

totalDistance = 0
locIDList1.sort();
locIDList2.sort();
differenceList = [abs(int(locIDList1[i]) - int(locIDList2[i])) for i in range(len(locIDList1))];
differnce = sum(differenceList)
print("distance : ", differnce);

# Part 2