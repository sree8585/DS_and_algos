# Some tomatoes stored in the warehouse are ripe, but some tomatoes may not yet be ripe. After a day to put in the box
# (M *N) from the storage, unripe tomatoes adjacent to the ripe tomatoes are ripe under the influence of ripe tomatoes.
# The adjacent place of one tomato means the tomato in the four directions: left, right, front, and back. Suppose that
# there is no effect on the diagonal tomatoes and that tomatoes do not ripen on their own.
#
# John wants to know how many days it will take for all tomatoes to be ripen.
# The size of the lattice-shaped boxes that store tomatoes in the warehouse and the information of ripe tomatoes and
# unripe tomatoes are given; some may not contain tomatoes.
# Create a program to find out how many days it takes for all tomatoes to ripen.
# Input
# Two integers M, N representing the size of the box are given to the first line; M represents the number of horizontal
# spaces of the box, N represents the number of vertical spaces of the box; 2 ≤ M, N ≤ 1,000.
# From the second line, the information of the tomatoes stored in one box is given, that is, from the second line
# to the N line, the information of the tomatoes in the box is given. In one line, the state of tomatoes in the box
# horizontal line is given as M integers.
# Number 1 represents ripe tomatoes, number 0 represents unripe tomatoes, and number -1 represents empty spaces.
#
#
# Output
# You have to print out the minimum date until the tomatoes are all ripe. If all tomatoes are already ripe,
# you have to output zero, and if the tomatoes are not ripe no matter how long, you have to output -1.


# Step 1: Take Input from Teminal
# Step 2: Initial Validation for all rippen or all unrippen or empty box.
#         If any of the condition satisfied print and return
#
# ## Will be running BFS with Little modifications as initially it can be collection of multiple networks/graphs
# Step 3: find all the initial positions of ripen tomatoes.
# Step 4: At each iteration until BFS queue is empty
#         remove a ripen tomato from queue.
#         check for all possible adjacent pos of a ripen tomato which is unripen and make it ripe.
#         Add to the queue
#         increment no. of days
# Step 5: Check if all the tomatoes are ripen.
#         If so, print number of days and return
#         else, return by printing -1

def ripeTomatoSolution():
    mn = input()
    mn = [int(i.strip()) for i in mn.split(" ")]
    row = mn[1]
    col = mn[0]
    boxOfTomatoes = []
    for i in range(row):
        rowVals = input()
        rowVals = [int(i.strip()) for i in rowVals.split(" ")]
        boxOfTomatoes.append(rowVals)

    allUnRipe = initialValidationForAllUnripeorEmpty(boxOfTomatoes)
    if allUnRipe:
        print(-1)
        return

    allRipe = validationForAllRipe(boxOfTomatoes)
    if allRipe:
        print (0)
        return


    queue, days = [], -1
    # look for all initial ripe tomatoes
    for i in range(row):
        for j in range(col):
            if boxOfTomatoes[i][j] == 1:
                queue.append((i, j))

    # run BFS
    while len(queue) > 0:
        for i in range(len(queue)):
            poppedRow, poppedCol = queue.pop(0)
            for x, y in [(poppedRow + 1, poppedCol), (poppedRow - 1, poppedCol), (poppedRow, poppedCol + 1),
                         (poppedRow, poppedCol - 1)]:
                if 0 <= x < row and 0 <= y < col and boxOfTomatoes[x][y] == 0:
                    boxOfTomatoes[x][y] = 1
                    queue.append((x, y))
        days += 1

    isAlRipe = validationForAllRipe(boxOfTomatoes)
    if isAlRipe:
        print(days)
    else:
        print (-1)

    return


def initialValidationForAllUnripeorEmpty(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] not in (0, -1):
                return False
    return True

def validationForAllRipe(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] not in (1 , -1):
                return False
    return True


ripeTomatoSolution()