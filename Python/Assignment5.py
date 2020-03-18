def camelcase_check(string):
    newstring = ''
    notfirst = 0
    for char in string:
        if char.isupper() and notfirst:
            newstring += ' ' + char
        else:
            newstring += char
        notfirst = 1
    print(newstring)







def main():
    camelcase_check('YoImSoCool')

if __name__ == '__main__':
    main()
