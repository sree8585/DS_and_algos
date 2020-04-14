# Input:
# BANANA APPLE
#
# Output:
#     BANANA
#     .P....
#     .P....
#     .L....
#     .E....
#
# Input:
#     TRIANGLE RECTANGLE
#
# Output:
#     R.......
#     E.......
#     C.......
#     TRIANGLE
#     A.......
#     N.......
#     G.......
#     L.......
#     E.......
#
# Input:
#     PLANET EARTH
#
# Output:
#     ..E...
#     PLANET
#     ..R...
#     ..T...
#     ..H...


def solution():
    a = 'BANANA'
    b = 'APPLE'
    intersection = findIntersection(a, b)
    print(intersection)
    printStrings(a, b, intersection)


def findIntersection(a, b):
    row = len(a)
    col = len(b)
    for i in range(row):
        for j in range(col):
            # print (a[j], b[i])
            if a[i] == b[j]:
                return (i, j)


def printStrings(a, b, intersection):
    intersectionAta = intersection[0]
    intersectionAtb = intersection[1]

    for j in range(len(b)):
        for i in range(len(a)):
            if j != intersectionAtb and i == intersectionAta:
                print(b[j], end='\t')
            elif j == intersectionAtb:
                print(a[i], end='\t')
            else:
                print('.', end='\t')
        print()


solution()
