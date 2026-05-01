import tail_recursive as tr
# Dvir Farkash 333228062
# question 1
def pentaNumRangeNonTail(n1, n2):
    getPentaNum = lambda n: 0.5 * n * (3*n - 1)
    if (n1 == n2):
        return []
    return pentaNumRangeNonTail(n1, n2 - 1) + [getPentaNum(n2 - 1)]

def pentaNumRangeTail(n1, n2):
    getPentaNum = lambda n: 0.5 * n * (3*n - 1)
    # the inner function calculates the range [n1,n2] and not the range [n2, n2)
    @tr.tail_recursive
    def pentaNumRange(n1, n2, result=[]):
        if (n1 == n2):
            return result
        else:
            return pentaNumRange(n1, n2-1, [getPentaNum(n2-1)] + result)
    if (n1 == n2):
        return []
    # the inner function calculates the range [n1,n2] and not the range [n2, n2), 
    # so the outer function returns the inner from n1 to n2-1
    return pentaNumRange(n1, n2)

def print1(func):
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
        return
        
    numbers = func(n1, n2)
    for i, num in enumerate(numbers):
        if (i != 0 and i % 10 == 0):
            print()
        print(num, end = " ")
    print()
    
def question1():
    tail = bool(int(input("If you want to use the tail version enter 1, otherwise enter 0: ")))
    print1(pentaNumRangeTail if tail else pentaNumRangeNonTail)


# question 2
def reverseNumNonTail(n):
    return int(''.join(reverseListNonTail(list(str(abs(n)))))) * (-1 if n < 0 else 1)
    
def reverseListNonTail(l):
    if (l == []):
        return []
    else:
        return [l[-1]] + reverseListNonTail(l[:-1])
    
def reverseNumTail(n):
    return int(''.join(reverseListTail(list(str(abs(n)))))) * (-1 if n < 0 else 1)

@tr.tail_recursive 
def reverseListTail(l, result = []):
    if (l == []):
        return result
    else:
        return reverseListTail(l[:-1], result + [l[-1]])
    
def print2(func):
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
    except ValueError:
        print("ERROR: Input number is incorrect")
        return
    
    print(func(n))
    
    if (func(n) != int(''.join(reversed(list(str(abs(n)))))) * (-1 if n < 0 else 1)):
        print("ERROR")
        
def question2():
    tail = bool(int(input("If you want to use the tail version enter 1, otherwise enter 0: ")))
    print2(reverseNumTail if tail else reverseNumNonTail)  
    
# question 3
def piNonTail(n):
    if (n == 1):
        return 4
    else:
        iTerm = lambda i: (((-1)**(i + 1)) / (2*i - 1))
        return 4*iTerm(n) + piTail(n - 1)
    
@tr.tail_recursive
def piTail(n, result = 0):
    if (n == 0):
        return result
    else:
        iTerm = lambda i: (((-1)**(i + 1)) / (2*i - 1))
        return piTail(n - 1, 4*iTerm(n) + result)

def print3(n, func, current = 1):
    print(f"{current} {func(current)}")
    if (current < n):
        print3(n, func, current + 1)
        
def question3():
    tail = bool(int(input("If you want to use the tail version enter 1, otherwise enter 0: ")))
    try:
        n = int(input("Enter a Natural number n: "))
    except ValueError:
        print("ERROR: Input number is incorrect!")
        return
    if (n < 1):
        print("ERROR: Input number is incorrect!")
        return
    print3(n, piTail if tail else piNonTail)
   
# question 4
# finding primes from 2 to n
def primesNonTail(n):
    return sieveNonTail(list(range(2, n + 1)))

def primesTail(n):
    return sieveTail(list(range(2, n + 1)))

# sieve of eratosthenes on list of numbers
def sieveNonTail(l):
    if (l == []):
        return []
    
    remaining = divisibleByNNonTail(l[0], l[1:])
    return [l[0]] + sieveNonTail(remaining)

@tr.tail_recursive
def sieveTail(l, result = []):
    if (l == []):
        return result
    
    remaining = divisibleByNTail(l[0], l[1:])
    return sieveTail(remaining, result + [l[0]])
# returns the divisible number by n in the list l
def divisibleByNNonTail(n, l):
    if (l == []):
        return []
    if (l[0] % n == 0):
        return divisibleByNNonTail(n, l[1:])
    else:
        return [l[0]] + divisibleByNNonTail(n, l[1:])

@tr.tail_recursive  
def divisibleByNTail(n, l, result = []):
    if (l == []):
        return result
    
    if (l[0] % n == 0):
        return divisibleByNTail(n, l[1:], result)
    else:
        return divisibleByNTail(n, l[1:], result + [l[0]])
    
def twinpNonTail(n):
    return twinpListNonTail(primesNonTail(n))

def twinpTail(n):
    return twinpListTail(primesTail(n))
    
# returns a dictionary with prime twins (the list should have all primes in some range ordered)
def twinpListNonTail(l):
    if (l == [] or len(l) == 1):
        return dict()
    
    if (l[1] - l[0] == 2):
        return {l[0]: l[1]} | twinpListNonTail(l[1:])
    else: 
        return twinpListNonTail(l[1:])

@tr.tail_recursive
def twinpListTail(l, result = dict()):
    if (l == [] or len(l) == 1):
        return result
    
    if (l[1] - l[0] == 2):
        return twinpListTail(l[1:], result | {l[0]: l[1]})
    else: 
        return twinpListTail(l[1:], result)

def question4():
    tail = bool(int(input("If you want to use the tail version enter 1, otherwise enter 0: ")))
    try:
        n = int(input("Enter a Natural number n: "))
    except ValueError:
        print("ERROR: Input number is incorrect!")
        return
    if (n < 1):
        print("ERROR: Input number is incorrect!")
        return
    print(listToStr4(list((twinpTail(n) if tail else twinpNonTail(n)).items())))
    
def listToStr4(l, result = ""):
    if (l == []):
        return result
    else:
        return listToStr4(l[1:], result + f"{l[0][0]} {l[0][1]}\n")
    
# question 5
def add3dictsNonTail(d1, d2, d3):
    allKeys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    getKeyTuple = lambda key: tuple(set(mymapNonTail(lambda d: d[key], myfilterNonTail(lambda d: key in d, [d1, d2, d3]))))
    getKeyVal = lambda key: (key, getKeyTuple(key) if len(getKeyTuple(key)) > 1 else  getKeyTuple(key)[0])
    
    return dict(mymapNonTail(getKeyVal, list(allKeys)))
  
def add3dictsTail(d1, d2, d3):
    allKeys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    getKeyTuple = lambda key: tuple(set(mymapTail(lambda d: d[key], myfilterTail(lambda d: key in d, [d1, d2, d3]))))
    getKeyVal = lambda key: (key, getKeyTuple(key) if len(getKeyTuple(key)) > 1 else  getKeyTuple(key)[0])
    
    return dict(mymapTail(getKeyVal, list(allKeys)))

def mymapNonTail(func, l):
    if (l == []):
        return []
    else:
        return [func(l[0])] + mymapNonTail(func, l[1:])
  
@tr.tail_recursive  
def mymapTail(func, l, result = []):
    if (l == []):
        return result
    else:
        return mymapTail(func, l[1:], result + [func(l[0])])
    
def myfilterNonTail(func, l):
    if (l == []):
        return []
    elif (func(l[0])):
        return [l[0]] + myfilterNonTail(func, l[1:])
    else:
        return myfilterNonTail(func, l[1:])
    
@tr.tail_recursive  
def myfilterTail(func, l, result = []):
    if (l == []):
        return result
    elif (func(l[0])):
        return myfilterTail(func, l[1:], result + [l[0]])
    else:
        return myfilterTail(func, l[1:], result)
    
def print5(func):
    try:
        dict1 = eval(input("Enter a dictionary: "))
        dict2 = eval(input("Enter a dictionary: "))
        dict3 = eval(input("Enter a dictionary: "))
    except ValueError:
        print("ERROR: Input is incorrect!")
        return    
    if (isinstance(dict1, dict) != True or isinstance(dict2, dict) != True or isinstance(dict3, dict) != True):
        print("ERROR: Input is incorrect!")
    else:
        print(func(dict1, dict2, dict3))

def question5():
    tail = bool(int(input("If you want to use the tail version enter 1, otherwise enter 0: ")))
    print5(add3dictsTail if tail else add3dictsNonTail)
    
# running
def main():
    lfuncs = [question1, question2, question3, question4, question5]
    lstrs = ["exit", "penta numbers", "reverse number", "pi series calculation", "twin primes", "merging dictionaries"]
    
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