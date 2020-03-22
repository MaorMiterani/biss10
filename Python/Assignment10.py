firstIteration = True

def find_second_x(lines):
    global firstIteration
    first = True

    templines = lines.copy()
    rownumber = 0
    for row in templines:
        if row.find('X') != -1 and first:
            row = row[row.find('X') + 1:]
            first = False
        if row.find('X') != -1:
            x = row.find('X')
        rownumber += 1
    else:
        return x, rownumber - 1


def line_valid(lines):
    global firstIteration
    currentLocation = []
    rowNumber = 0
    horizontal = False
    vertical = False
    tupleList = []
    if not firstIteration:
        x, y = find_second_x(lines)
        value = lines[y][x]
    else:
        for row in lines:
            if row.find('X') != -1:
                currentLocation.append(row.find('X'))
                currentLocation.append(rowNumber)
                x = currentLocation[0]
                y = currentLocation[1]
                value = lines[y][x]
                break
            else:
                rowNumber += 1
    prevX = x
    prevY = y
    tupleList.append((x,y))
    if x + 1 < len(lines[y]) and lines[y][x + 1] != '|' and lines[y][x + 1] != ' ':
        x += 1
        value = lines[y][x]
        horizontal = True

    elif x - 1 > 0 and lines[y][x - 1] != '|' and lines[y][x - 1] != ' ':
        x -= 1
        value = lines[y][x]
        horizontal = True

    elif y + 1 < len(lines) and lines[y + 1][x] != '-' and lines[y + 1][x] != ' ':
        y += 1
        value = lines[y][x]
        vertical = True

    elif y - 1 > 0 and lines[y - 1][x] != '-' and lines[y - 1][x] != ' ':
        y -= 1
        value = lines[y][x]
        vertical = True

    else:
        return False

    while value != 'X':
        if value == '-' and horizontal:
            if x - 1 == prevX:
                prevX = x
                x += 1
                value = lines[y][x]
            elif x + 1 == prevX:
                prevX = x
                x -= 1
                value = lines[y][x]
            tupleList.append((x, y))
        elif value == '|' and vertical:
            if y - 1 == prevY:
                prevY = y
                y += 1
                value = lines[y][x]
            elif y + 1 == prevY:
                prevY = y
                y -= 1
                value = lines[y][x]
            tupleList.append((x, y))
        elif value == '+' and horizontal:
            horizontal = False
            vertical = True
            if y + 1 < len(lines) and lines[y + 1][x] != '-' and lines[y + 1][x] != ' ' and not (x, y + 1) in tupleList and (y - 1 == -1 or (not lines[y - 1][x] == ' ' and (x, y - 1) in tupleList)):
                prevY = y
                y += 1
                value = lines[y][x]


            elif y - 1 >= 0 and lines[y - 1][x] != '-' and lines[y - 1][x] != ' ' and not (x, y - 1) in tupleList and (y + 1 >= len(lines) or (not lines[y + 1][x] == ' ' and (x, y + 1) in tupleList)):
                prevY = y
                y -= 1
                value = lines[y][x]

            else:
                break
            tupleList.append((x, y))

        elif value == '+' and vertical:
            horizontal = True
            vertical = False
            if x + 1 < len(lines[y]) and lines[y][x + 1] != '|' and lines[y][x + 1] != ' ' and not (x + 1, y) in tupleList and (x - 1 == -1 or (not lines[y][x - 1] == ' ' and (x - 1, y) in tupleList)):
                prevX = x
                x += 1
                value = lines[y][x]

            elif x - 1 >= 0 and lines[y][x - 1] != '|' and lines[y][x - 1] != ' ' and not (x - 1, y) in tupleList and (x + 1 >= len(lines[y]) or (not lines[y][x + 1] == ' ' and (x + 1, y) in tupleList)):
                prevX = x
                x -= 1
                value = lines[y][x]

            else:
                break
            tupleList.append((x, y))
        if value == ' ':
            break
    else:
        return True

    if firstIteration:
        firstIteration = False
        return False or line_valid(lines)
    else:
        return False










'''
line_valid(grid)  # ---> True
grid = ["     ",
        "  X  ",
        "  |  ",
        "  |  ",
        "  X  "]
line_valid(grid)  # ---> True
# Note: this grid is only valid when starting on the right-hand X, but still considered valid
grid = ["                      ",
        "   +-------+          ",
        "   |      +++---+     ",
        "X--+      +-+   X     "]
line_valid(grid)  # ---> True
grid = [" X  ",
        " |  ",
        " +  ",
        " X  "]
line_valid(grid)  # ---> False
grid = ["              ",
        "   +------    ",
        "   |          ",
        "X--+      X   ",
        "              "]
line_valid(grid)  # ---> False
grid = ["      +------+",
        "      |      |",
        "X-----+------+",
        "      |       ",
        "      X       "]
line_valid(grid)  # ---> False
'''

def main():
    print(line_valid(["      +------+",
        "      |      |",
        "X-----+------+",
        "      |       ",
        "      X       "]))


if __name__ == '__main__':
    main()
