# Dvir Farkash 333228062
# question 2 import
import MenuForTar1
# question 5 import
import question5
# import random
import random

# question 1:
def verifyTriangleLengths(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def question1():
    print("Please enter the lengths of the triangle:")
    a = float(input())
    b = float(input())
    c = float(input())
    if (verifyTriangleLengths(a, b, c)):
        print("correct triangle sides lengths")
    else:
        print("not correct triangle sides lengths")

# question 3:
def printMiddle4Sort(a,b,c,d):
    list = [a,b,c,d]
    
    list.sort()
    
    print (f"{list[1]}, {list[2]}")
    
def printMiddle4NoSort(a,b,c,d):
    list = [a,b,c,d]
    
    list.remove(max(list))
    list.remove(min(list))
    
    print (f"{list[0]}, {list[1]}")
    
def printMiddleSort(numbers):
    sortedList = sorted(numbers)
    
    middleIndex = len(sortedList)//2
    
    print(f"{sortedList[middleIndex-1]}, {sortedList[middleIndex]}")
    
def printMiddleNoSort(numbers):
    for i in range((len(numbers) // 2) - 1):
        numbers = tuple(list(numbers).remove((max(numbers))))
        numbers = tuple(list(numbers).remove((min(numbers))))
    print(f"{list[0]}, {list[1]}")
 
def printMiddle(list):
    numbers = extractNumbers(list)
    printMiddleSort(numbers)
    
def question3():
    exampleTuple = (34, 15, 32, 67, "my test", 40, ['abc', 35, 20], 100)
    printMiddle(exampleTuple)

def extractNumbers(listParam):
    numbers = []
    for item in listParam:
        if isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, (list, tuple)):
            numbers.extend(extractNumbers(item))
    return numbers

# question 4:
def shiftL(binNr, N):
    result = binNr[N:] + '0' * N
    return result

def shiftR(binNr, N):
    result = '0' * N + binNr[:-N]
    return result

def shiftCL(binNr, N):
    result = binNr[N:] + binNr[:N]
    return result

def shiftCR(binNr, N):
    result = binNr[-N:] + binNr[:-N]
    return result 

def question4():
    print(f"shiftL 2 of 1101100101: {shiftL('1101100101', 2)}")
    print(f"shiftR 2 of 1101100101: {shiftR('1101100101', 2)}")
    print(f"shiftCL 2 of 1101100101: {shiftCL('1101100101', 2)}")
    print(f"shiftCR 2 of 1101100101: {shiftCR('1101100101', 2)}")

# question 6
def nihushTest(randomNumbers, nihush):
    result = tuple()
    for i, num in enumerate(nihush):
        if (num == randomNumbers[i]):
            result += (num,)
        else:
            result += ("X",)
    return result

def pct(result):
    correct = 0
    for elm in result:
        if isinstance(elm, int):
            correct += 1
    return (correct / len(result)) * 100

def printTuple(tupleToPrint, end = "\n"):
    print("[", end = "")
    for i, elm in enumerate(tupleToPrint):
        print(elm, end = "")
        if (i + 1 != len(tupleToPrint)):
            print(", ", end = "")
    print("]", end = "")

def question6():
    length = random.randint(3,9)
    maxpct = 0
    randomNumbers = tuple()
    for i in range(length):
        randomNumbers += (random.randint(1,9),)
    
    num = 0
    while(True):
        nihush = tuple()
        for i in range(length):
            num = int(input("Enter a number for a guess:\n"))
            if (num == -1):
                break
            nihush += (num,)
        if (num == -1):
            break
        result = nihushTest(randomNumbers, nihush)
        printTuple(result)
        print(f", The correct guesses percentage is: {pct(result)}")
        if (maxpct < pct(result)):
            maxpct = pct(result)
        if (maxpct == 100):
            break
    
    print("The random numbers: ", end="")
    printTuple(randomNumbers)
    print(f"\nThe maximum percentage of the guesses: {maxpct}")

# running
def main():
    lfuncs = [question1, MenuForTar1.question2, question3, question4, question5.question5, question6]
    lstrs = ["exit", "question 1: verify triangle sides lengths", "question 2: area and volume of different shapes", "question 3: print middle values", "question 4: shift numbers", "question 5: counting types", "question 6: guessing numbers"]
    
    while True:
        print("your choices:")
        for (i,s) in enumerate(lstrs):
            print(i, " : ", s)
        c = int(input("please enter your choice "))
        if c==0:
            break
        elif c>=1 and c<=len(lstrs):
            lfuncs[c-1]()
        else:
            print ("error")
   

if __name__ == "__main__":
    main()