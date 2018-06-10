
def makeArrayConsecutive2(statues):
    statues.sort()
    return (statues[-1]-statues[0])-len(statues)+1





print(makeArrayConsecutive2([6,2,3,8]))