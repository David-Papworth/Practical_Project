import random 

def points():
    difficulty = 10
    difficulty_strat = 20
    lower_points = 0
    higher_points = 50
    lower_points += difficulty
    higher_points += difficulty
    lower_points += difficulty_strat
    higher_points += difficulty_strat
    return random.randrange(lower_points, higher_points)

print(points())