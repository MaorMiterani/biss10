def filter_even(numlist):
    evenlist = []
    for number in numlist:
        if not number % 2:
            evenlist.append(number)
    return evenlist

def main():
    print(filter_even([23,453,75,24,64,233,1246]))

if __name__ == "__main__":
    main()
