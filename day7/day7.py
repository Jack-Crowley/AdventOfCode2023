with open("./day7/day7.txt") as data: data = [i.strip() for i in data.readlines()]

def scoreHand(hand):
    cards = "23456789TJQKA"
    score = 0

    if hand.count(hand[0]) == 5:
        score+=10**14
    for card in hand:
        if hand.count(card) == 4: 
            score+=10**13
        if hand.count(card) == 3: 
            score+=10**12
        if hand.count(card) == 2: 
            score+=10**11

    return score+int("".join([f"{cards.index(card):02d}" for card in hand]))

def part1(data=data):
    hands = [[x.split()[0], int(x.split()[1])] for x in data]

    hands.sort(key=lambda x: scoreHand(x[0]))

    return sum([(i+1)*v[1] for i,v in enumerate(hands)])

def scoreP2(hand):
    cards = "J23456789TQKA"
    bestScore = 0
    for c in cards:
        score = f"{scoreHand(hand.replace('J', c)):020d}"
        score = int(score[:10]+"".join([f"{cards.index(card):02d}" for card in hand]))
        bestScore = max(score, bestScore)
    return bestScore

def part2(data=data):
    hands = [[x.split()[0], int(x.split()[1])] for x in data]

    hands.sort(key=lambda x: scoreP2(x[0]))

    return sum([(i+1)*v[1] for i,v in enumerate(hands)])

SampleInput = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

p1 = part1()
print("Part 1: ", p1)

p2 = part2()
print("Part 2: ", p2)