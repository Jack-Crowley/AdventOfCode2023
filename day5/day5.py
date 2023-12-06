import itertools
import collections
import heapq
import math
import functools

with open("./day5/day5.txt") as data: data = [i.strip() for i in data.read().split("\n\n")]


def part1(data=data):
    seeds = collections.defaultdict(lambda: {"seed":None, "soil": None, "fertilizer": None, "water": None, "light": None, "temperature": None, "humidity": None, "location":None})

    for i in data[0].split(": ")[1].split():
        seeds[i]["seed"] = int(i)

    for elements in data[1:]:
        elements = elements.split("\n")
        sour,des = elements[0].split()[0].split("-to-")
        for line in elements[1:]:
            d,s,r = [int(i) for i in line.split()]
            ran = range(s, s+r+1)
            for v in seeds.values():
                if int(v[sour]) in ran:
                    v[des] = v[sour]-s+d
        for v in seeds.values():
            v[des] =  v[des] if v[des] != None else v[sour]

    return min([v["location"] for v in seeds.values()])

def part2(data=data):
    ranges = []

    seeds = data[0].split(": ")[1].split()

    for i in range(0, len(seeds), 2):
        ranges.append([int(seeds[i]), int(seeds[i])+int(seeds[i+1])])

    for elements in data[1:]:
        currRanges = []

        elements = elements.split("\n")
        for line in elements[1:]:
            d,s,r = [int(i) for i in line.split()]
            for i in range(len(ranges)-1,-1,-1):
                start,end = ranges[i]
                startRange = start if s <= start else s
                endRange = end if s+r >= end else s+r

                if startRange > end or endRange < start:
                    continue

                del ranges[i]
                ranges.append([start, startRange])
                ranges.append([endRange, end])
                currRanges.append([startRange-s+d, endRange-s+d])

        for v in ranges:
            if v[0] != v[1]:
                currRanges.append(v)

        ranges = currRanges
    return min([x[0] for x in ranges])

SampleInput = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
SampleInput = [i.strip() for i in SampleInput.split("\n\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)