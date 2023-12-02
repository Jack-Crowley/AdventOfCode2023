with open("./day1/day1.txt") as data: data = [i.strip() for i in data.readlines()]

def part1(data=data):
    counter = 0
    
    for i in data:
        f,l = -1,-1
        for x in i:
            if x.isdigit():
                if f == -1: f= x
                l = x
        counter+=int(f+l)

    return counter


def part2(data=data):
    counter = 0

    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in data:
        f,l = -1,-1
        for v,x in enumerate(i):
            if x.isdigit():
                if f == -1: f= x
                l = x
            for v1,num in enumerate(nums):
                if i[v:].startswith(num):
                    if f == -1: f= str(v1+1)
                    l = str(v1+1)
        counter+=int(f+l)

    return counter

SampleInput = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)