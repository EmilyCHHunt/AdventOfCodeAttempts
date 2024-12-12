# Day 5 of the 2024 advent of code programming puzzles
# @author Emily Chesterton-Hunt
#
def readFile():
    # inputFile = open("testInp");
    inputFile = open("input");
    inputText = inputFile.read();
    return inputText


def splitParts(inputText):
    inputList = inputText.split('\n')
    splitLoc = inputList.index('');

    rulesList = inputList[:splitLoc]
    printOrderList = inputList[splitLoc + 1:]

    rules = []
    printOrder = []
    for rule in rulesList:
        rules.append(rule.split("|"))
    for prints in printOrderList:
        printOrder.append(prints.split(","))

    return rules, printOrder;


def calculateValidity(rulesList, printOrderList):
    total = 0;

    for printOrder in printOrderList:
        failed = False;
        for i in range(0, len(printOrder)):
            for rule in rulesList:
                if rule[0] == printOrder[i]:
                    for j in range(0, len(printOrder)):
                        if rule[1] == printOrder[j] and not failed:
                            if j < i:
                                failed = True;
        if not failed:
            total += int(printOrder[(len(printOrder) // 2)]);

    return total;




if __name__ == '__main__':
    rulesList, printOrderList = splitParts(readFile());
    print(calculateValidity(rulesList, printOrderList))