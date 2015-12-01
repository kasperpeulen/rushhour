from rushhour import hash_table
from rushhour.breath_first_search import breath_search
from rushhour.games import games
import rushhour.hash_table

game_index = int(input("Which game do you want to solve? "))

game = games[game_index - 1]

print("Trying to solve game with breadth first algortihm... ")

breath_search(game)

print("We can simplify this problem by \"freezing\" some cars.")
freeze_cars = list(map(int, input("Tell me which cars to freeze: (e.g.: 10, 14, 16) ").split(", ")))

freeze_cars = [game.cars[i] for i in freeze_cars]

for car in freeze_cars:
    car.immobile = True

for car in game.cars:
    print(car.immobile)

breath_search(game)