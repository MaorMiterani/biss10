def check_password(passwordlist):
    passwordlist = passwordlist.split(',')
    for password in passwordlist:
        lowercase = False
        number = False
        uppercase = False
        specialChar = False
        if len(password) > 6 and len(password) < 12:
            for char in password:
                if char.islower():
                    lowercase = True
                if char in '0123456789':
                    number = True
                if char.isupper():
                    uppercase = True
                if char in '@#$%^&*':
                    specialChar = True
        if lowercase and number and uppercase and specialChar:
            print(password)







def main():
    check_password(input())


if __name__ == '__main__':
    main()
