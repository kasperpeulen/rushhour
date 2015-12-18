import hash_table
from benchmark import BenchMark
from board import Board, Win
from car import Car
from typing import Dict, List


def a_star_search(initial: Board, depth, admissable=False):
    BenchMark.start_the_time()
    try:
        _a_star_search(initial, depth, admissable)
    except Win:
        BenchMark.log_time()
        BenchMark.log_states_count()
        exit(0)


def _a_star_search(initial: Board, depth, admissable=False):
    """
    Breath First Search algorithm. Also shows steps, new states and total states.
    """
    Car.boardWidth = initial.board_width
    Car.boardHeight = initial.board_height
    Board.a_star_depth = depth
    hash_table.states_checked_hash_table = {}
    queue = {}
    star_value = initial.a_star_count(admissable)
    queue[star_value] = [initial]
    print(initial)

    while True:
        best_boards = find_best_boards(queue)
        for best_board in best_boards:
            next_boards = best_board.possible_next_boards()
            for board in next_boards:
                value = board.a_star_count(admissable)
                if value not in queue:
                    queue[value] = [board]
                else:
                    queue[value].append(board)

        BenchMark.steps_made += 1
        print("")
        BenchMark.log_steps_made()
        BenchMark.log_time()
        BenchMark.log_states_count()


def find_best_boards(queue: Dict) -> List[Board]:
    minimum = min(queue.keys(), key=int)
    best_boards = queue[minimum]
    BenchMark.states_count += len(best_boards)
    del queue[minimum]
    return best_boards
