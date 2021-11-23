import random


def valorant():
    valo = ['Omen', 'Jett', 'Raze', 'Skye', 'Yoru', 'Astra', 'Kay/O', 'Chamber', 'Brimstone',
            'Phoenix', 'Sage', 'Sova', 'Viper', 'Cypher', 'Reyna', 'Killjoy', 'Breach']
    return random.choice(valo)

def guns():
    guns = ['Classic', 'Ghost', 'Frenzy', 'Shorty', 'Sheriff', 'Stinger', 'Spectre', 'Bucky', 'Judge', 'Guardian', 'Bulldog', 'Phantom', 'Vandal', 'Marshal', 'Operator', 'Ares', 'Odin']
    return random.choice(guns)

def dice():
    return random.randint(1, 6)


def number_selector(a):
    res = [int(i) for i in a.split() if i.isdigit()]
    n = random.randint(res[0], res[1])
    return n
