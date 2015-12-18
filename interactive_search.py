import hash_table

from board import Win
from breath_first_search import breath_search
from games import games
from position import Position

def interactive_search(game_index):
    game = games[game_index - 1]

    print("Trying to solve game with breadth first algortihm... ")
    print("If I can't solve it in 10 seconds, I'll ask for your help.")

    breath_search(game, 10)
    print("We can simplify this problem by \"freezing\" some cars.")

    while True:
        for car in game.cars:
            car.immobile = False

        change_goal = bool(input("Do you want to change the goal? True/False "))
        if change_goal:
            index = int(input("Give the index of the goal car: (e.g.: 2) "))
            position = list(map(int, input("Give the position of the goal: (e.g.: 2,3) ").split(",")))
            position = Position.new(position[0], position[1])
            game.goal = (index, position)
        freeze_cars = list(map(int, input("Tell me which cars to freeze: (e.g.: 10, 14, 16) ").split(", ")))

        freeze_cars = [game.cars[i] for i in freeze_cars]


        for car in freeze_cars:
            car.immobile = True

        total_time = int(input("How long do want to run? "))
        try:
            breath_search(game, total_time)
        except Win as win:
            save = bool(input("You won! Do you want to save this game and proceed? True/False "))
            if save:
                game = win.board
