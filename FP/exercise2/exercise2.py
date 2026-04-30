# Dvir Farkash 333228062
# question 1
def pentaNumRange(n1, n2):
    getPentaNum = lambda n: 0.5 * n * (3*n - 1)
    return list(map(getPentaNum, range(n1, n2)))

def unfunctionalPrint():
    try:
        n1 = int(input("enter the value of n1: "))
        n2 = int(input("enter the value of n1: "))
    except ValueError:
        print("ERROR: the input should be integers")
        return
    if (n1 < 1 or n2 < 1):
        print("ERROR: the values must be positive integers and n2 > n1")
        return
    if (n1 >= n2):
        print("ERROR: the values must be positive integers and n2 > n1")
        
    numbers = pentaNumRange(n1, n2)
    for i, num in enumerate(numbers):
        if (i != 0 and i % 10 == 0):
            print()
        print(num, end = " ")
    print()
    
# this is the functional function in question 1
def functional1(n1, n2):
    if (n1 >= n2 or n1 < 1 or n2 < 1):
        return "ERROR: the values must be positive integers and n2 > n1"
    
    # gets the numbers
    numbers = pentaNumRange(n1, n2)
    
    str_numbers = list(map(str, numbers))
    
    if (n2 - n1 <= 10):
        return " ".join(str_numbers[:])
    else: 
        # every 10 numbers inserts a '\n'
        return " ".join(str_numbers[0 : 10]) + "\n" + functional1(n1 + 10, n2)
    
# this is unfunctional function for the I/O part
def question1():
    try:
        n1 = int(input("enter the value of n1: "))
        n2 = int(input("enter the value of n2: "))
    except ValueError:
        print("ERROR: the input should be integers")
        return
    if (n1 < 1 or n2 < 1):
        print("ERROR: the values must be positive integers and n2 > n1")
        return
    if (n1 >= n2):
        print("ERROR: the values must be positive integers and n2 > n1")
        
    print(functional1(n1, n2))
    
# question 2
def sumDigits(n):
    def gettingDigits(n):
        if (n < 10):
            return [n]
        else:
            return [n % 10] + gettingDigits(n // 10)
    return sum(gettingDigits(abs(n)))

def question2():
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        print(sumDigits)
    except (ValueError):
        print("ERROR: Input number is incorrect!")
    
# question 3
def isPalindrome(n):
    reverseNumber = lambda n: int(str(n)[::-1])
    return n == reverseNumber(n)

def question3():
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        print("It is a palindrome" if isPalindrome(n) else "It is not a palindrome")
    except (ValueError):
        print("ERROR: Input number is incorrect!")

# question 4
def m(n):
    def firstNTerms(n):
        iTerm = lambda i: i / (i + 1)
        return list(map(iTerm, range(1, n + 1)))
    return sum(firstNTerms(n))

def question4():
    try:
        n = int(input("Enter a Natural number n: "))
        if (n < 1):
            raise ValueError
        print("\n".join(map(lambda n: f"{n} {m(n)}", range(1, n + 1))))
    except ValueError:
        print("ERROR: Input number is incorrect!")
    
# running
def main():
    lfuncs = [question1, question2, question3, question4]
    lstrs = ["exit", "penta numbers", "sum digits", "palindrome check", "series claculation"]
    
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