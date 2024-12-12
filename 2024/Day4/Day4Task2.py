# Day 4 task 2 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
#
# The goal of this task was to find MAS as an X in the wordsearch
# M.S
# .A.
# M.S
def readFile():
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText


def stringToList(text):
    return text.split('\n')

# Searches the word search for the centre of the target word and calls searchLine to get all strings from that point
# then every possible direction of the worlds
def wordSearch(wordSearchList, targetWord):
    wordNum = 0;
    for y in range(len(wordSearchList)):
        for x in range(len(wordSearchList[y])):
            if wordSearchList[y][x] == "A":
                surroundingWords = searchLine(wordSearchList, x, y);

                if ((surroundingWords[0] == targetWord or surroundingWords[0] == "SAM") and
                            (surroundingWords[1] == targetWord or surroundingWords[1] == "SAM")):
                    print(surroundingWords)
                    wordNum += 1;

    return wordNum;

# Finds all valid strings coming from the given coordinate ( diagonals) and returns them as a list
def searchLine(wordSearchList, x, y):
    foundStrings = ["", ""];

    if 1 <= y <= len(wordSearchList) - 2 and 1 <= x <= len(wordSearchList[y]) - 2:
        for i in range(-1,2):
                foundStrings[0] += (wordSearchList[y + i][x + i]);
        for i in range(-1,2):
                foundStrings[1] += (wordSearchList[y + i][x - i]);
    # print(foundStrings);
    return foundStrings;


if __name__ == '__main__':
    inputWordSearch = stringToList(readFile());
    print(wordSearch(inputWordSearch, "MAS"));
