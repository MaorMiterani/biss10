import string

filename = 'bigsecret.txt'



file = open(filename, 'r')
cipher = file.read().split(',')

for char in cipher:
    newlist = list(map(lambda x: int(x), cipher))

elementList1 = newlist[0::3] # Z
elementList2 = newlist[1::3] # A
elementList3 = newlist[2::3] # Z

keyList = list(string.ascii_lowercase)
availableKeys = keyList.copy()

for i in keyList:    # I used this method on each list to check for the number of spaces
    numberofspaces = 0
    for char in elementList3:
        decrypted = chr(char ^ ord(i))
        if decrypted == ' ' and i in availableKeys:
            numberofspaces += 1

solution = []
on1 = True
on2 = False
on3 = False

for i in range(len(newlist)):
    if on1:
        solution.append(chr(newlist[i] ^ ord('Z')))
        on1 = False
        on2 = True
    elif on2:
        solution.append(chr(newlist[i] ^ ord('A')))
        on2 = False
        on3 = True
    elif on3:
        solution.append(chr(newlist[i] ^ ord('Z')))
        on3 = False
        on1 = True

print(''.join(solution))
