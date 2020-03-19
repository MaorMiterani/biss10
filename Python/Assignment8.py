def dejumble (messy, correctlist):
    dictCheck = {}
    returnList = []
    for word in correctlist:
        for char in word:
            if char in dictCheck:
                dictCheck[char] += 1
            else:
                dictCheck[char] = 1
        tempDict = dictCheck.copy()
        for char in messy:
            if char in tempDict:
                tempDict[char] -= 1
        for char in tempDict:
            if tempDict[char] <= 0:
                break
        else:
            returnList.append(word)
    return returnList



def main():
    print(dejumble('ppge',['ppgedgsg']))


if __name__ == '__main__':
    main()
