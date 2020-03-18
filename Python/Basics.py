def targil_1(list1, list2):
    tuplelist = []
    while list1 and list2:
        tuplelist.append((list1.pop(0), list2.pop(0)))
    print(tuplelist)
    return tuplelist

def targil_2(tuplelist):
    tupledict = {}
    while tuplelist:
        temptuple = tuplelist.pop(0)
        tupledict[temptuple[0]] = temptuple[1]
    print(tupledict)
    return tupledict

def targil_4(list1, list2):
    listDict = {}
    while list1 and list2:
        listDict[list1.pop(0)] = list2.pop(0)
    print (listDict)
    return listDict

def main():
    for2 = targil_1([3,45,78,23,65], [64,72,54,12])
    targil_2(for2)
    targil_4([3,45,78,23,65], [64,72,54,12])


if __name__ == '__main__':
    main()
