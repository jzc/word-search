def printArray(array):
    for r in array:
        for c in r:
            print(c),
            print(' '),
        print

def transpose(array):
    row = len(array)
    col = len(array[0])
    t = [[0 for c in range(row)] for r in range(col)]
    for r in range(row):
        for c in range(col):
            t[c][r] = array[r][c]
    return t

def solve(array, words):
    row = len(array)
    col = len(array[0])
    t = transpose(array)
    east = []
    eastC = []
    south = []
    southC = []
    sw = []
    swC = []
    for r in range(row):
        s = ''
        sC = []
        for c in range(col):
            s += array[r][c]
            sC.append([r,c])
        east.append(s)
        eastC.append(sC)
    for r in range(col):
        s = ''
        sC = []
        for c in range(row):
            s += t[r][c]
            sC.append([c,r])
        south.append(s)
        southC.append(sC)
    for i in reversed(range(row)):
        s= ''
        sC = []
        for j in range(row-i):
            if not j >= col:
                s += array[i+j][j]
                sC.append([i+j,j])
        sw.append(s)
        swC.append(sC)
    for i in reversed(range(1,col)):
        s = ''
        sC = []
        for j in range(col-i):
            if not j > row:
                s += t[i+j][j]
                sC.append([j,i+j])
        sw.append(s)
        swC.append(sC)
    
    print(east)
    print(south)
    print(sw)
    print(eastC)
    print(southC)
    print(swC)
    
    coordinates = []
    for w in words:
        for i, item in enumerate(east):
            if w in item:
                coordinates.append([eastC[i][item.index(w)],eastC[i][item.index(w)+len(w)-1]])
        for i, item in enumerate(south):
            if w in item:
                coordinates.append([southC[i][item.index(w)],southC[i][item.index(w)+len(w)-1]])
        for i, item in enumerate(sw):
            if w in item:
                coordinates.append([swC[i][item.index(w)],swC[i][item.index(w)+len(w)-1]])
        
    print
    print coordinates
    return coordinates
    
        
array = [['1','2','3','4'],['5','6','7','8'],['9','0','1','2'],['3','4','5','6']]
printArray(array)
#printArray(transpose(array))
solve(array, ['234','616', '13'])