# question 1
def pentaNumRange(n1, n2):
    getPentaNum = lambda n: 0.5 * n * (3*n - 1)
    return list(map(getPentaNum, range(n1, n2)))

def unfunctionalPrint():
    try:
        n1 = int(input("please enter two number n1, n2:\n"))
        n2 = int(input())
    except ValueError:
        print("ERROR: the input should be integers")
        return
    if (n1 < 1 or n2 < 1):
        print("ERROR: the numbers should be positive")
        return
    if (n1 >= n2):
        print("ERROR: n2 should be bigger than n1")
        
    numbers = pentaNumRange(n1, n2)
    for i, num in enumerate(numbers):
        if (i != 0 and i % 10 == 0):
            print()
        print(num, end = " ")
    print()
        
def functoinal(n1, n2):
    pass

def question1():
    pass
    
        

# running
def main():
    lfuncs = []
    lstrs = ["exit"]
    
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
    unfunctionalPrint()
    main()