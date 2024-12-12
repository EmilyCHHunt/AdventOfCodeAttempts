def readFile():
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText


def stringToList(text):
    return text.split('\n')


def wordSearch(wordSearchList, targetWord):
    wordNum = 0;
    for y in range(len(wordSearchList)):
        for x in range(len(wordSearchList[y])):
            if wordSearchList[y][x] == "X":
                surroundingWords = searchLine(wordSearchList, x, y);

                for words in surroundingWords:
                    if words == targetWord:
                        wordNum += 1;

    return wordNum;


def searchLine(wordSearchList, x, y):
    foundStrings = ["", "", "", "", "", "", "", ""];
    if x <= len(wordSearchList[y]) - 4:
        for i in range(0, 4):
            foundStrings[0] += (wordSearchList[y][x + i]);
    if x >= 3:
        for i in range(0, 4):
            foundStrings[1] += (wordSearchList[y][x - i]);
    if y <= len(wordSearchList) - 4:
        for i in range(0, 4):
            foundStrings[2] += (wordSearchList[y + i][x]);

        if x >= 3:
            for i in range(0, 4):
                foundStrings[4] += (wordSearchList[y + i][x - i]);
        if x <= len(wordSearchList[y]) - 4:
            for i in range(0, 4):
                foundStrings[5] += (wordSearchList[y + i][x + i]);
    if y >= 3:
        for i in range(0, 4):
            foundStrings[3] += (wordSearchList[y - i][x]);

        if x >= 3:
            for i in range(0, 4):
                foundStrings[6] += (wordSearchList[y - i][x - i]);
        if x <= len(wordSearchList[y]) - 4:
            for i in range(0, 4):
                foundStrings[7] += (wordSearchList[y - i][x + i]);

    return foundStrings;


if __name__ == '__main__':
    inputWordSearch = stringToList(readFile());
    print(wordSearch(inputWordSearch, "XMAS"));
