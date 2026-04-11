# Dvir Farkash 333228062
#question 5:
def countTypes(countList):
    result = {"int": 0, "float": 0, "str": 0, "list": 0, "tuple": 0, }
    for elm in countList:
        if isinstance(elm, int):
            result["int"] += 1
        if isinstance(elm, float):
            result["float"] += 1
        if isinstance(elm, str):
            result["str"] += 1
        if isinstance(elm, list):
            result["list"] += 1
        if isinstance(elm, tuple):
            result["tuple"] += 1
    
    return result

def question5():
    inputList = [1, 2, 'a', (11,2,'b'), [22,'c'], (33,), ['d'], 'e']
    result = countTypes(inputList)
    
    if (result["tuple"]):
        print("סה\"כ הרשומות:", end=" ")
        print(f"{result["tuple"]},", end=" ")
    if (result["list"]):
        print("סה\"כ רשימות:", end=" ")
        print(f"{result["list"]},", end=" ")
    if (result["int"]):
        print("סה\"כ המספרים השלמים:", end=" ")
        print(f"{result["int"]},", end=" ")
    if (result["str"]):
        print("סה\"כ המחרוזות:", end=" ")
        print(f"{result["str"]},", end=" ")
    if (result["float"]):
        print("סה\"כ המספרים העשרוניים:", end=" ")
        print(f"{result["float"]},", end=" ")
    
if (__name__ == "__main__"):
    question5()