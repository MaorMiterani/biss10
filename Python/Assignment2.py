string = input()
temp = string.split(' ')
i = 0
for word in temp:
    if i % 2:
        temp.remove(word)
        temp.insert(i, 'biss10')
    i += 1
string = ' '.join(temp)
print(string)
