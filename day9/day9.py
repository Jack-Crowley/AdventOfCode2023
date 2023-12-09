with open("./day9/day9.txt") as data: data = [i.strip() for i in data.readlines()]

def getSequenceP1(numbers):
    if all([i == 0 for i in numbers]):
        return 0
    return getSequenceP1([numbers[i+1]-numbers[i] for i in range(len(numbers)-1)])+numbers[-1]

def part1(data=data):
    counter = 0
    
    for i in data:
        nums = [int(x) for x in i.split()]
        counter+=getSequenceP1(nums)

    return counter

def getSequenceP2(numbers):
    if all([i == 0 for i in numbers]):
        return 0
    return numbers[0]-getSequenceP2([numbers[i+1]-numbers[i] for i in range(len(numbers)-1)])

def part2(data=data):
    counter = 0
    
    for i in data:
        nums = [int(x) for x in i.split()]
        counter+=getSequenceP2(nums)

    return counter

SampleInput = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)