import collections
import math

with open("./day3/day3.txt") as data: data = [[x for x in i.strip()] for i in data.readlines()]

def part1(data=data):
    counter = 0

    for lIndex, line in enumerate(data):
        curr="0"
        part = False
        for cIndex, char in enumerate(line):
            if char.isdigit():
                curr+=char
                for [x,y] in [[x1,y1] for y1 in [-1,0,1] for x1 in [-1,0,1]]:
                    x,y = cIndex+x,lIndex+y
                    if not (0<=x<len(data[0]) and 0<=y<len(data)): continue
                    c = data[y][x]
                    if c != "." and not c.isdigit():
                        part = True
            else:
                if part: counter+=int(curr)
                curr="0"
                part = False
        if part:
            counter+=int(curr)
    return counter

def part2(data=data):
    counter = 0

    gears = collections.defaultdict(set)
    nums = []

    for lIndex, line in enumerate(data):
        curr=""

        for cIndex, char in enumerate(line):
            if char.isdigit():
                curr+=char
                for [x,y] in [[x1,y1] for y1 in [-1,0,1] for x1 in [-1,0,1]]:
                    x,y = cIndex+x,lIndex+y
                    if not (0<=x<len(data[0]) and 0<=y<len(data)): continue
                    c = data[y][x]
                    if c == "*":
                        gears[(y,x)].add(len(nums))
            else:
                if curr != "": nums.append(curr)
                curr=""

        if curr != "": nums.append(curr)

    for v in gears.values():
        if len(v) == 2:
            counter+=math.prod([int(nums[x]) for x in list(v)])
    return counter

SampleInput = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
SampleInput = [[x for x in i.strip()] for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)