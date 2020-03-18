import sys

def remove_unwanted_characters(string):
    unwanted = '!@#"$%^[]--{?}&*,\n()_+;=:\'`.'
    for char in string:
        if (char in unwanted):
            string = string.replace(char,' ')
    return string.lower()

def return_dictionary(words):
    wordsDict = {}
    for word in words:
        if word not in wordsDict.keys():
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1
    return wordsDict

def file_handling(filename):
    book = open(filename, 'r')
    words = book.read()
    words = remove_unwanted_characters(words)
    words = words.split(' ')
    return words

def print_words(filename):
    words = file_handling(filename)
    words.sort()
    wordsDict = return_dictionary(words)
    for word in wordsDict:
        print(word + ' ' + str(wordsDict[word]))

def print_top(filename):
    words = file_handling(filename)
    wordsDict = return_dictionary(words)
    wordsDict = {words: word for words, word in sorted(wordsDict.items(), key=lambda item: item[1], reverse=True)[:20]}
    for word in wordsDict:
        print(word + ' ' + str(wordsDict[word]))



def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | ---topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)

    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
