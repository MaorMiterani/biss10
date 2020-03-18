def dejumble(messy, correctlist):
    returnlist = []
    for word in correctlist:
        for char in messy:
            if word.find(char) == -1:
              break
        else:
            returnlist.append(word)
    return returnlist







def main():
    print(dejumble('ortsp',['sport', 'parrot', 'ports', 'matey']))

if __name__ == '__main__':
    main()
