def dejumble(messy, correctlist):
    returnlist = []
    for word in correctlist:
        temp = messy
        for char in word:
            if temp.find(char) == -1:
              break
            else:
                temp = temp.replace(char, '' , 1)
        else:
            returnlist.append(word)
    return returnlist





def main():
    print(dejumble('ortsp',['sport', 'parrot', 'ports', 'matey']))


if __name__ == '__main__':
    main()
