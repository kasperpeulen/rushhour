from rushhour import hash_table
from rushhour.board import Board, Win
from rushhour.car import Car
from rushhour.games import level1, game5, game4, game2, game7, game1, game6, \
    game3
from typing import Dict, List
import time


def a_star_search(initial: Board):
    """
    Breath First Search algorithm. Also shows steps, new states and total states.
    """
    Car.boardWidth = initial.board_width
    Car.boardHeight = initial.board_height
    hash_table.states_checked_hash_table = {}
    queue = {}
    star_value = initial.a_star_count()
    queue[star_value] = [initial]
    print(initial)

    while True:
        best_boards = find_best_boards(queue)
        for best_board in best_boards:
            next_boards = best_board.possible_next_boards()
            for board in next_boards:
                value = board.a_star_count()
                if value not in queue:
                    queue[value] = [board]
                else:
                    queue[value].append(board)
        print(queue.keys())


def find_best_boards(queue: Dict) -> List[Board]:
    best_boards = queue[min(queue.keys(), key=int)]
    del queue[min(queue.keys(), key=int)]
    return best_boards

start = time.time()
try:
    a_star_search(game4)
except Win as win:
    end = time.time()
    print(end - start)
    exit(0)
    print("you won")