import math

with open("./day6/day6.txt") as data: data = [i.strip() for i in data.readlines()]

def part1(data=data):
    counter = 1

    times = [int(i) for i in data[0].split(":")[1].split()]
    distances = [int(i) for i in data[1].split(":")[1].split()]

    for i,t in enumerate(times):
        d = distances[i]
        a=0
        for x in range(t):
            if (t-x)*x > d:
                a+=1
        counter*=a if a > 0 else 1

    return counter

def part2(data=data):
    time = int("".join(data[0].split(":")[1].split()))
    distance = int("".join(data[1].split(":")[1].split()))

    b,c = -time, distance

    low = (-b - (b**2 - 4*c)**.5)/2
    high = (-b + (b**2 - 4*c)**.5)/2

    return math.floor(high)-math.ceil(low)+1

SampleInput = """"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)