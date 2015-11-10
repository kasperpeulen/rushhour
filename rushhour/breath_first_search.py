import time

from rushhour.board import Board, Win
from rushhour.games import game2, level1, game4
from rushhour.hash_table import states_checked_hash_table

def breath_search(initial: Board):

    # initial board (stage 0)
    path = []
    path.append([initial])
    print(initial)
    states_checked_hash_table[hash(initial)] = [initial]
    print("step 1")
    count = 1
    while True:
        nextPath = []
        for board in path[-1]:
            try:
                nextPath.extend(board.possible_next_boards())
            except Win:
                end = time.time()
                print(end - start)
        print(len(nextPath))
        print(time.time() - start)
        count += 1
        print("step ", count)
        path.append(nextPath)


    # for board in path2:
    #     print(board)
    # print(len(path2))
    # for board in path[-1]:
    #     print(board)
    # print(states_checked_hash_table)
    #

start = time.time()
breath_search(game4)
