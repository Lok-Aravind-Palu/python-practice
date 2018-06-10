

input = [3, 6, -2, -5, 7, 3]

def adjacent(inputarray):
    z = inputarray[0]*inputarray[1]
    for x in range(len(inputarray)-1):
        a = inputarray[x]
        b = inputarray[x+1]
        s = a*b
        if s>z:
            z = s
    return z





print(adjacent(input))


# or

def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])