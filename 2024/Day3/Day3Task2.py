# Day 3 task 2 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
#
# Task2 follows on from task1 with the addition of do() and don't()
# Which enable and disable mul() functions
def readFile():
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText;


# Searches the string for all cases where there are mul functions and stores the index in a list
#
# @params corrupted string, functions to search for
# @returns array of indexes
def findFunc(inputText, funcToSearch):
    index_of_mul = 0;
    indexToSearch = 0;
    funcStarts = [];
    while not index_of_mul == -1:
        index_of_mul = inputText.find(funcToSearch, indexToSearch);
        indexToSearch = index_of_mul + 1

        if index_of_mul != -1:
            funcStarts.append(index_of_mul);
    return funcStarts;

# Finds the state of the mult function by finding whether it is closer to a do or dont function
#
# Parameters Index of the current mult function, list of all unseen dos, list of all unseen donts
# Returns whether the boolean is true
def checkState(curIndex, doStarts, dontStarts):

    if len(dontStarts) == 0:
        return True;
    if len(doStarts) == 0:
        return False;
    doDistance = curIndex - int(doStarts[0])
    dontDistance = curIndex - int(dontStarts[0])
    if dontDistance > doDistance > 0 or dontDistance < 0:
        if (dontDistance > 0):
            del dontStarts[0];
        return True;
    else:
        if (doDistance > 0):
            del doStarts[0];
        return False;


# Checks for any corruption in the function
#
# @params corrupted string, list of function indexes
# @return 2d array of integers from uncorrupted string
def checkForErrors(inputText, mulStarts, dostarts, dontStarts):
    products = []

    for mulStart in mulStarts:
        errorHasOccurred = False;
        reachedEnd = False;
        numbersToMultiply = [""]
        curIndex = mulStart + 4;
        enabled = checkState(mulStart, dostarts, dontStarts);
        print(enabled);
        if not curIndex > len(inputText) and enabled:
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

    mulStarts = findFunc(inputText, "mul(");
    doStarts= (findFunc(inputText, "do()"));
    doStarts.insert(0, 0);
    dontStarts = findFunc(inputText, "don't()");

    extractedNumbers = checkForErrors(inputText, mulStarts, doStarts, dontStarts)
    print(extractedNumbers);
    print(calculateTotal(extractedNumbers));
