def almostIncreasingSequence(sequence):
    seq = sorted(sequence)
    count = 0
    for x,y in enumerate(sequence):
        if y == seq[x]:
            count +=1
            print(seq[x])
    return count % 2 == 0


print(almostIncreasingSequence([1,3,2,1]))


