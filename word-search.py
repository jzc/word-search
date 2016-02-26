import random

def printArray(array):
    for r in array:
        for c in r:
            print(c),
        print

def transpose(array):
    row = len(array)
    col = len(array[0])
    t = [[0 for c in range(row)] for r in range(col)]
    for r in range(row):
        for c in range(col):
            t[c][r] = array[r][c]
    return t
    
def rotate90(array):
    transposed = transpose(array)
    rotated = []
    for i in transposed:
        rotated.append(list(reversed(i)))
    return rotated
    
#Returns the diagonals of half an array
#Offset cuts off that amount of diagonals, e.g. 0 will do n diagonals, 1 will do n-1 diagonals
def diagonals(array, coordinateArray, offset):
    diagonals = []
    coordinates = []
    rowCount = len(array)
    columnCount = len(array[0])
    for n in range(rowCount - offset):
        string = ''
        coords = []
        if n > columnCount:
            n = columnCount
        for k in range(n, -1 , -1):
            string += array[k][n-k]      
            coords.append(coordinateArray[k][n-k])    
        diagonals.append(string)
        coordinates.append(coords)
    return [diagonals,coordinates]

def findWord(stringArray, coordinateArray, word):
    coords = []
    for n, string in enumerate(stringArray):
            startIndex = string.find(word)
            if not startIndex == -1:
                endIndex = startIndex + len(word) - 1
                coords.append([coordinateArray[n][startIndex], coordinateArray[n][endIndex]])
    if not len(coords) == 0:
        return coords
    else:
        return -1;
        
def flatten2D(array):
    result = []
    for r in array:
        for c in r:
            result.append(c)
    return result

#Array contains a 2d array with the grid of characters, words is an array with the strings to look for
def solve(array, words):

    #These arrays contain the combined string of each direction
    rowCount = len(array)
    columnCount = len(array[0])
    south = []
    east = []
    se = []
    ne = []
    
    #Contain coordinates for each direction
    southCoords = []
    eastCoords = []
    seCoords = []
    neCoords = []
    coordinates = []
    
    for i in range(rowCount):
        row = []
        for j in range(columnCount):
            row.append([i,j])
        coordinates.append(row)

    #Transformed arrays
    transposed = transpose(array)
    rotated90 = rotate90(array)
    rotated180 = rotate90(rotated90)
    rotated270 = rotate90(rotated180)
    
    #Transformed coordinate arrays
    transposedCoords = transpose(coordinates)
    rotated90Coords = rotate90(coordinates)
    rotated180Coords = rotate90(rotated90Coords)
    rotated270Coords = rotate90(rotated180Coords)
    
    #east
    for i, row in enumerate(array):
        string = ''
        coords = []
        for j, element in enumerate(row):
            string += element
            coords.append(coordinates[i][j])
        east.append(string)
        eastCoords.append(coords)
    
    #south
    for i, row in enumerate(transposed):
        string = ''
        coords = []
        for j, element in enumerate(row):
            string += element
            coords.append(transposedCoords[i][j])
        south.append(string)
        southCoords.append(coords)
    
    #ne
    diags = diagonals(array, coordinates, 0)
    ne.append(diags[0])
    neCoords.append(diags[1])
    
    diags = diagonals(transpose(rotated180), transpose(rotated180Coords), 1)
    ne.append(diags[0])
    neCoords.append(diags[1])
    
    ne = flatten2D(ne)
    neCoords = flatten2D(neCoords)
    
    #se
    diags = diagonals(transpose(rotated90), transpose(rotated90Coords), 0)
    se.append(diags[0])
    seCoords.append(diags[1])
    
    diags = diagonals(rotated270, rotated270Coords, 1)
    se.append(diags[0])
    seCoords.append(diags[1])
    
    se = flatten2D(se)
    seCoords = flatten2D(seCoords)
    
    print "Solutions"
    solution = []
    for word in words:
        coords = []
        value = findWord(east, eastCoords, word)
        if not value == -1:
            coords = value
        value = findWord(south, southCoords, word)
        if not value == -1:
            coords = value
        value = findWord(ne, neCoords, word)
        if not value == -1:
            coords = value
        value = findWord(se, seCoords, word)
        if not value == -1:
            coords = value
        if not len(coords) == 0:
            solution.append(coords)
        else:
            solution.append(-1)    
        print word, coords
        
array = [['1','2','3','4'],['5','6','7','8'],['9','0','1','2'],['3','4','5','6']]
printArray(array)
solve(array, ['50' , '307', '34'])