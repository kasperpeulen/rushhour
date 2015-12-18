import time

import hash_table
from benchmark import BenchMark
from board import Board, Win
from car import Car
from games import game2, level1, game4, game5, game6, game1


def countPath(paths):
    """
    Count every step in tree (depth).
    """
    count = 0
    for p in paths:
        count += len(p)
    return count


def breath_search(initial: Board, total_time: int):
    """
    Breath First Search algorithm. Also shows steps, new states and total states.
    """
    hash_table.states_checked_hash_table = {}
    BenchMark.start_the_time()
    Car.boardWidth = initial.board_width
    Car.boardHeight = initial.board_height
    # initial board (stage 0)
    path = []
    path.append([initial])

    hash_table.states_checked_hash_table[hash(initial)] = [initial]

    print("initial state: ")
    print(initial)

    while True:
        nextPath = []
        for board in path[-1]:
            try:
                nextPath.extend(board.possible_next_boards())
            except Win:
                BenchMark.states_count = countPath(path)
                BenchMark.log_steps_made()
                BenchMark.log_time()
                BenchMark.log_states_count()
                return
                # exit(0)


        path.append(nextPath)

        BenchMark.states_count = countPath(path)
        BenchMark.steps_made += 1
        print("")
        BenchMark.log_steps_made()
        BenchMark.log_time()
        BenchMark.log_states_count()


        if len(nextPath) == 0:
            print("States space is explored, no solution found...")
            print("Try freezing less cars.")
            return
        print(time.time() - BenchMark.start_time)
        if (time.time() - BenchMark.start_time) > total_time:
            print("This game is too hard for me! Aborting ....")
            return
