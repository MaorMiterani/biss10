import functools
print(functools.reduce(lambda x,y: x + y, range(1,11)))

def check_palindrome(number):
    return True if number == int(str(number)[::-1]) else False

def factorial(number):
    return functools.reduce(lambda x,y: x*y, map(lambda x: number - x, range(number)))

def main():
    print(check_palindrome(554455))
    print(factorial(5))


if __name__ == '__main__':
    main()
