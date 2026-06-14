# Dvir Farkash 333228062
# question 1
def evenprt(n1, n2, n3):
    def enterGenerator(iter, n):
        for i in enumerate(iter):
            yield f"{i[1]} " if (i[0] + 1) % n != 0 else f"{i[1]}\n"
    isEven = lambda x: x % 2 == 0
    result = (n for n in range(n1, n2 + 1) if isEven(n))
    return "".join(enterGenerator(result, n3))

def question1():
    try:
        n1 = int(input("Enter the value of N1: "))
        n2 = int(input("Enter the value of N2: "))
        n3 = int(input("Enter the value of N3: "))
        if (n1 >= n2 or n3 >= (n2 - n1)):
            raise ValueError
        print(evenprt(n1, n2, n3))
    except ValueError:
        print("ERROR: at least one of the input values is incorrect")
        
# question 2
def primefactors(n):
    primeNum = napa(n)
    return (i for i in range(1, int(n / 2) + 1) if (i in primeNum and n % i == 0))

def napa(n):
    setOfNonPrimes = set([val for i in range(2, n+1) for val in divisibleByN(i, n) ])
    return [i for i in range(1, n+1) if (i not in setOfNonPrimes)]
def divisibleByN(n, maxNum):
    return [i for i in range(1, maxNum + 1) if (i % n == 0 and i != n)]

def question2():
    try:
        n = int(input("Enter a positive number: "))
        if(n <= 0):
            raise ValueError
        print(list(primefactors(n)))
    except ValueError:
        print("ERROR: the number must be a positive integer")
        
# question 3
def sortedzip(listOfSubLists):
    return zip(*(sorted(i, key=str) for i in listOfSubLists))

def reversedzip(listOfSubLists):
    return zip(*(reversed(i) for i in listOfSubLists))

def funczip(func, listOfSubLists):
    return list(func(listOfSubLists))

def unzippy(zipLists):
    tupleResult = zip(*zipLists)
    return list((list(i) for i in tupleResult))

def question3():
    try:
        size = int(input("Enter the size of the sublists of the list to process: ")) 
        if (size < 1):
            raise ValueError
    except ValueError:
        print("ERROR - The size should be an integer!")
        return
    
    try:
        listOfSubLists = eval(input("Enter the list to process: "))
    except SyntaxError:
        print("ERROR - The input should be a valid")
        return 
    
    if (False in (len(i) == size for i in listOfSubLists)):
        print(f"ERROR - all sublists must be of size {size}")
        return
    
    funcs = {
        1: sortedzip,
        2: reversedzip
    }
    
    print("1: sortedzip")
    print("2: reversedzip")
    
    try:
        funcNum = int(input("Which function do you want to choose? "))
    except ValueError:
        print("ERROR - The input should be the number of the function")
        return
    
    try:
        result = funczip(funcs[funcNum], listOfSubLists)
        print(result)
        print(unzippy(result))
    except KeyError:
        print("ERROR - chosen function does not exist.")

# running
def main():
    lfuncs = [question1, question2, question3]
    lstrs = ["exit", "print even numbers", "prime factors", "zip functions"]
    
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