# question 2 import
import MenuForTar1

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


# running
def main():
	lfuncs = [question1, MenuForTar1.question2, question3]
	lstrs = ["exit", "question 1: verify triangle sides lengths", "question 2: area and volume of different shapes", "question 3: print middle values"]

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
   

if __name__ =="__main__":
	main()