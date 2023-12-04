with open("./day4/day4.txt") as data: data = [i.strip() for i in data.readlines()]

def part1(data=data):
    counter = 0
    
    for i in data:
        winners, hand = i.split(": ")[1].split(" | ")
        winners = [int(i) for i in winners.split()]
        hand = [int(i) for i in hand.split()]

        x = .5

        for l in hand:
            if l in winners:
                x*=2
        
        counter += x if x!=.5 else 0

    return int(counter)

def part2(data=data):
    
    cards = []

    for i in data:
        winners, hand = i.split(": ")[1].split(" | ")
        winners = [int(i) for i in winners.split()]
        hand = [int(i) for i in hand.split()]

        x = 0
        for b in hand:
            if b in winners:
                x+=1

        cards.append(x)
    
    totals = [1]*len(cards)

    for i,v in enumerate(cards):
        for x in range(i+1, i+v+1):
            totals[x]+=totals[i]

    return sum(totals)

SampleInput = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)