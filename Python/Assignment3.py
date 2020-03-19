def filter_even(numlist):

    return list(filter(lambda x: x % 2 == 0, numlist))

def main():
    print(filter_even([23,453,75,24,64,233,1246]))

if __name__ == "__main__":
    main()
