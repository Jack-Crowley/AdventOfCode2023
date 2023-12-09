import itertools
import collections
import heapq
import math
import functools

with open("./day8/day8.txt") as data: data = [i.strip() for i in data.readlines()]

def part1(data=data):
    counter = 0
    
    nodes = {}

    instructions = list(data[0])
    directions = "LR"

    for i in data[2:]:
        key, pair = i.split(" = (")

        item1, item2 = pair.split(", ")
        item2 = item2[:-1]

        nodes[key] = [item1, item2]

    currIndex = "AAA"

    while not currIndex.endswith("Z"):
        currInstruction = directions.index(instructions[counter % len(instructions)])
        currIndex = nodes[currIndex][currInstruction]
        counter+=1

    return counter


def part2(data=data):
    counter = 0
    
    nodes = {}

    instructions = list(data[0])
    directions = "LR"

    currIndex = []
    for i in data[2:]:
        key, pair = i.split(" = (")

        item1, item2 = pair.split(", ")
        item2 = item2[:-1]

        if key.endswith("A"):
            currIndex.append(key)

        nodes[key] = [item1, item2]

    zLoop = []

    for i in currIndex:
        counter = 0
        while not i.endswith("Z"):
            currInstruction = directions.index(instructions[counter % len(instructions)])
            i = nodes[i][currInstruction]
            counter+=1
        zLoop.append(counter)

    return math.lcm(*zLoop)

SampleInput = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)