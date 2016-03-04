import random     
import string
   
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
        return [];
        
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
        for coord in value:
            if not len(coord) == 0:
                coords.append(coord)
        value = findWord(south, southCoords, word)
        for coord in value:
            if not len(coord) == 0:
                coords.append(coord)
        value = findWord(ne, neCoords, word)
        for coord in value:
            if not len(coord) == 0:
                coords.append(coord)
        value = findWord(se, seCoords, word)
        for coord in value:
            if not len(coord) == 0:
                coords.append(coord)
        if not len(coords) == 0:
            solution.append(coords)
        else:
            solution.append(-1)    
        print word, coords
    return solution

#Pass the direction as string
def passThrough(startingCoord, length, direction, intersection):
    if direction == "east":
        if startingCoord[0] == intersection[0]:
            endingCoord = startingCoord[1] + length - 1
            if (intersection[1] >= startingCoord[1]) and (intersection[1] <= endingCoord):
                return True
        return False
    elif direction == "south":
        if startingCoord[1] == intersection[1]:
            endingCoord = startingCoord[0] + length - 1
            if (intersection[0] >= startingCoord[0]) and (intersection[0] <= endingCoord):
                return True
        return False
    elif direction == "ne":
        endingCoord = [startingCoord[0] + length - 1, startingCoord[1] - length + 1]
        x0 = startingCoord[0]
        y0 = startingCoord[1]
        xf = endingCoord[0]
        yf = endingCoord[1]
        xi = intersection[0]
        xf = intersection[1]
        if(x0 * (yf - yi) - y0 () / 2 == 0):
            return True
        return False
    elif direction == "se":
        return False
        
def placeWord(coordinateArray, word, rows, columns, invalidCoords, puzzle):
    for coord in coordinateArray:
            r = range(4)
            random.shuffle(r)
            for i in r:
                #east
                if i == 0: 
                    if (coord[1] + len(word) <= columns):
                        valid = True
                        for invalidCoord in invalidCoords:
                            if(passThrough(coord, len(word), "east", invalidCoord)):
                                valid = False
                                break
                        if valid:
                            for j, char in enumerate(word):
                                puzzle[coord[0]][coord[1] + j] = char 
                            return
                #south
                elif i == 1:
                    if (coord[0] + len(word) <= rows):
                        valid = True
                        for invalidCoord in invalidCoords:
                            if(passThrough(coord, len(word), "west", invalidCoord)):
                                valid = False
                                break
                        if valid:
                            for j, char in enumerate(word):
                                puzzle[coord[0] + j][coord[1]] = char 
                            return
                #ne
                elif i == 2:
                    if (coord[0] - len(word) >= -1) and (coord[1] + len(word) <= columns):
                        valid = True
                        for invalidCoord in invalidCoords:
                            if(passThrough(coord, len(word), "east", invalidCoord)):
                                valid = False
                                break
                        if valid:
                            for j, char in enumerate(word):
                                puzzle[coord[0] - j][coord[1] + j] = char 
                            return
                #se
                else:
                    if (coord[0] + len(word) <= columns) and (coord[1] + len(word) <= rows):
                        valid = True
                        for invalidCoord in invalidCoords:
                            if(passThrough(coord, len(word), "east", invalidCoord)):
                                valid = False
                                break
                        if valid:
                            for j, char in enumerate(word):
                                puzzle[coord[0] + j][coord[1] + j] = char 
                            return
        
#Creates a word search with the a given array of words, rows, and columns
def createPuzzle(words, rows, columns, challenge):
    while(True):
        puzzle = [['' for c in range(columns)] for r in range(rows)]
        #Iterate through each word
        for word in words:
            #Create a list of invalid coordinates, the word placed in the puzzle CANNOT pass through these.
            invalidCoords = []
            for i, row in enumerate(puzzle):
                for j, letter in enumerate(row):
                    if not letter == '' and not letter in word:
                        invalidCoords.append([i,j])
            #Randomly cycle through coordinates in the puzzle and attempt to place the word
            coordinateArray = []
            for r in range(rows):
                for c in range(columns):
                    coordinateArray.append([r,c])
            random.shuffle(coordinateArray)
            for coord in invalidCoords:
                coordinateArray.remove(coord)
            placeWord(coordinateArray, word, rows, columns, invalidCoords, puzzle)
        #Place random letters in the rest of the puzzle
        for i, row in enumerate(puzzle):
            for j, char in enumerate(row):
                if char == '':
                    if not challenge:
                        puzzle[i][j] = random.choice(string.ascii_lowercase)
                    else:
                        letters = ''
                        for word in words:
                            letters += word
                        puzzle[i][j] = random.choice(letters)
        solution = solve(puzzle, words)
        valid = True
        for coordList in solution:
            if coordList == -1:
                valid = False
                break
            if not len(coordList) == 1:
                valid = False
                break
        if valid:
            break          
    return puzzle         
                
array = [['1','2','3','4'],['5','6','7','8'],['9','0','1','2'],['3','4','5','6']]
printArray(array)
solve(array, ['34' , '307', 'a'])
words = ["kayak"]
puzzle = createPuzzle(words, 15, 15, True)
printArray(puzzle)