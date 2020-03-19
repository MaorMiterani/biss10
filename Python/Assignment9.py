import re

def check_password(passwordlist):
    passwordlist = passwordlist.split(',')
    special = re.compile('[@#$%^&*]')
    for password in passwordlist:
        lowercase = False
        number = False
        uppercase = False
        specialChar = False
        if len(password) > 6 and len(password) < 12:
            if re.findall('[a-z]', password):
                lowercase = True
            if re.findall('[0-9]', password):
                number = True
            if re.findall('[A-Z]', password):
                uppercase = True
            if re.findall('[@#$%^&*]', password):
                specialChar = True
        if lowercase and number and uppercase and specialChar:
            print(password)



def main():
    check_password(input())


if __name__ == '__main__':
    main()
