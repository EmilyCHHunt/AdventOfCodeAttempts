# Day 3 task 1 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
#
# Task1 requires a "corrupted" text file be read and from it we must find uncorrupted mul functions
# In the format mul(x,y) which we then calculate and add to a total
def readFile():
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText;


# Searches the string for all cases where there are mul functions and stores the index in a list
#
# @params corrupted string
# @returns array of indexes
def findMuls(inputText):
    indexOfMul = 0;
    indexToSearch = 0;
    mulStarts = [];
    while not indexOfMul == -1:
        indexOfMul = inputText.find("mul(", indexToSearch);
        indexToSearch = indexOfMul + 1

        if indexOfMul != -1:
            mulStarts.append(indexOfMul);
    return mulStarts;


# Checks for any corruption in the function
#
# @params corrupted string, list of function indexes
# @return 2d array of integers from uncorrupted string
def checkForErrors(inputText, mulStarts):
    products = []

    for mulStart in mulStarts:
        errorHasOccurred = False;
        reachedEnd = False;
        numbersToMultiply = [""]
        curIndex = mulStart + 4;

        if not curIndex > len(inputText):
            while not errorHasOccurred and not reachedEnd:
                if inputText[curIndex] == ")":
                    if len(numbersToMultiply) > 1:
                        reachedEnd = True;
                    else:
                        numbersToMultiply = [];
                        errorHasOccurred = True;

                elif 48 <= ord(inputText[curIndex]) <= 57:
                    numbersToMultiply[-1] += (inputText[curIndex]);

                elif (inputText[curIndex]) == ",":
                    if len(numbersToMultiply) >= 2:
                        errorHasOccurred = True;
                        numbersToMultiply = [];
                    else:
                        numbersToMultiply.append("");
                else:
                    errorHasOccurred = True;
                curIndex += 1;
            if (len(numbersToMultiply)) > 0 and not errorHasOccurred:
                products.append(numbersToMultiply);
    return products;


def calculateTotal(extractedNumbers):
    total = 0;
    for nums in extractedNumbers:
        total += multiply(nums);
    return total;


def multiply(nums):
    return int(nums[0]) * int(nums[1]);


if __name__ == '__main__':
    inputText = readFile();
    mulStarts = findMuls(inputText);
    extractedNumbers = checkForErrors(inputText, mulStarts)
    print(extractedNumbers);
    print(calculateTotal(extractedNumbers));
