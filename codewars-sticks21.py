import random
def makeMove(sticks):
    game = sticks % 4
    if game == 0:
        return random.randint(1, 3)
    return game
