# Rush Hour Solver 

Solves your rush hour puzzles.

For example:

```
python3 rushhour.py --game 2 --bfs
```

Runs game2 with breadth first search.

We have two a* heuristics. For the most simple A star heuristic:

```
python3 rushhour.py --game 2 --astar --depth 1
```

The other A* heuristic, searches for blocking cars one level deeper:

```
python3 rushhour.py --game 2 --astar --depth 2
```

For the interactive freezing algorithm, use:

```
python3 rushhour.py --game 7 --interactive
```

