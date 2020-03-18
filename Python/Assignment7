def pilot():
    instruction = input()
    yAxis = 0
    xAxis = 0
    while instruction != '0':
        instruction , axis = instruction.split(' ')
        if instruction == 'UP':
            yAxis += int(axis)
        elif instruction == 'DOWN':
            yAxis -= int(axis)
        elif instruction == 'RIGHT':
            xAxis += int(axis)
        elif instruction == 'LEFT':
            xAxis -= int(axis)
        instruction = input()
    distance = int(abs(yAxis/xAxis))
    print (distance)



def main():
    pilot()

if __name__ == '__main__':
    main()
