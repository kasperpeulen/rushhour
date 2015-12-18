import argparse

import math

from interactive_search import interactive_search
from a_star import a_star_search
from breath_first_search import breath_search
from games import game4, game1, game2, game3, game5, game6, games


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--game", help="Specify the game number, e.g. --game 4",
                    type=int)

    parser.add_argument("-b", "--bfs", help="Run program using breadth first search.",
                    action="store_true")

    parser.add_argument("-a", "--astar", help="Run program using A star algortihm.",
                    action="store_true")

    parser.add_argument("-d", "--depth", help="Depth of the a star algorithm.",
                    type=int)

    parser.add_argument("-n", "--not_admissable", help="Set this flag, if you want a not addmissable a start algorithm.",
                    action="store_true")

    parser.add_argument("-i", "--interactive", help="Run program with interactive freezing.",
                    action="store_true")
    args = parser.parse_args()

    if args.bfs:
        breath_search(games[args.game - 1], math.inf)
    elif args.astar:
        a_star_search(games[args.game - 1], args.depth, not args.not_admissable)
    elif args.interactive:
        interactive_search(args.game)
    else:
        print("Please add either the --bfs flag or --astar flag.")

if __name__ == '__main__':
    main()