# question 1
def evenprt(n1, n2, n3):
    isEven = lambda x: x % 2 == 0
    result = (n for n in range(n1, n2) if isEven(n))


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
    main()