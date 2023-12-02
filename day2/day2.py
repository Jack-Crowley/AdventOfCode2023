import math

with open("./day2/day2.txt") as data: data = [i.strip() for i in data.readlines()]

def part1(data=data):
    counter = 0

    maxes = {"red": 12, "green":13,"blue":14}

    for i in data:
        head, info = i.split(": ")
        gameID = int(head[5:])

        b=True

        for game in info.split("; "):
            for color in game.split(", "):
                n,c = color.split(" ")
                n = int(n)
                if n > maxes[c]:
                    b = False
                    break
            if not b: break
        
        if b:
            counter+=gameID

    return counter

def part2(data=data):
    counter = 0
    

    for i in data:
        head, info = i.split(": ")
        gameID = int(head[5:])

        maxes = {"red": 0, "green":0,"blue":0}

        for game in info.split("; "):
            for color in game.split(", "):
                n,c = color.split(" ")
                n = int(n)
                if (maxes[c] < n): maxes[c] = n
        counter+=math.prod([v for k,v in maxes.items()])
    return counter

SampleInput = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: Your answer to Part 1 is", p1)

p2 = part2()
print("Part 2: Your answer to Part 2 is", p2)