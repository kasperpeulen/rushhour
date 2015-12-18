import os
import math

import hash_table
from car import Car
from position import Position
from typing import List, Dict
from termcolor import colored, RESET

class MegaCar:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        if start.y == end.y:
            self.horizontal = True
            self.length = abs(end.x - start.x)
        else:
            self.horizontal = False
            self.length = abs(end.y - start.y)

        self.positions = [start]
        for i in range(1, self.length):
            if self.horizontal:
                self.positions.append(start + Position.new(i, 0))
            else:
                self.positions.append(start + Position.new(0, i))
        self.positions.append(end)

    def no_clash(self, other_car: 'Car') -> bool:
        """
        Check if car clashes with specific car.
        """
        other_start = other_car.start
        other_end = other_car.end

        return not (self.end.x >= other_start.x and
                    self.start.x <= other_end.x and
                    self.end.y >= other_start.y and
                    self.start.y <= other_end.y)

    def no_clash_all_cars(self, other_cars: List['Car']) -> List['Car']:
        """
        Check if new car clashes with other cars (list).
        """
        result = []
        for other_car in other_cars:
            if not self.no_clash(other_car):
                result.append(other_car)
        return result

    def move(self, steps: int) -> 'MegaCar':
        """
        Move car "step" amount of places.
        """
        if self.horizontal:
            return Car.new(self.start + Position.new(steps, 0), self.horizontal,
                           self.length)
        else:
            return Car.new(self.start + Position.new(0, steps), self.horizontal,
                           self.length)

    @staticmethod
    def from_board(board: 'Board'):
        (index, goal_pos) = board.goal
        car_to_move = board.cars[index]
        if car_to_move.horizontal:
            if goal_pos.x < car_to_move.start.x:
                mega_car_start = Position.new(car_to_move.start.x - 1, car_to_move.start.y)
            else:
                mega_car_start = Position.new(car_to_move.end.x + 1, car_to_move.end.y)
        else:
            if goal_pos.y < car_to_move.start.y:
                mega_car_start = Position.new(car_to_move.start.x, car_to_move.start.y - 1)
            else:
                mega_car_start = Position.new(car_to_move.end.x, car_to_move.end.y + 1)

        mega_car = MegaCar(
            min(mega_car_start, goal_pos),
            max(mega_car_start, goal_pos)
        )
        return mega_car

    @staticmethod
    def from_goal(goal: (int, Position), cars: List[Car]):
        (index, goal_pos) = goal
        car_to_move = cars[index]
        if car_to_move.horizontal:
            if goal_pos.x < car_to_move.start.x:
                mega_car_start = Position.new(car_to_move.start.x - 1, car_to_move.start.y)
            else:
                mega_car_start = Position.new(car_to_move.end.x + 1, car_to_move.end.y)
        else:
            if goal_pos.y < car_to_move.start.y:
                mega_car_start = Position.new(car_to_move.start.x, car_to_move.start.y - 1)
            else:
                mega_car_start = Position.new(car_to_move.end.x, car_to_move.end.y + 1)

        mega_car = MegaCar(
            min(mega_car_start, goal_pos),
            max(mega_car_start, goal_pos)
        )
        return mega_car

    def __str__(self) -> str:
        """
        Visualize the car in the board. C means there is a car at that position, X means there is no car
        """
        s = "\n"
        for y in range(0, Car.boardHeight):
            for x in range(0, Car.boardWidth):
                if Position.new(x, y) in self.positions:
                    s += "C "
                else:
                    s += "X "
            s += "\n"
        return s



class Board:
    """
    Board definition
    """

    a_star_depth = 0

    def __init__(self, board_width: int, board_height: int, cars: List['Car'],
                 goal: (int, Position), previous=None):
        """
        Define values for board. Previous is parental state for path checking.
        """
        self.board_height = board_height
        self.board_width = board_width
        self.previous = previous
        if previous is not None:
            self.count = previous.count + 1
        else:
            self.count = 0
        self.cars = cars
        self.goal = goal
        self.moves = ""

    def is_winner(self) -> bool:
        """
        Check if car is at goal (board exit).
        """
        (index, position) = self.goal
        return self.cars[index].end == position

    def possible_next_boards(self):
        """
        Define new possible boards (states).
        """
        new_boards = []
        for i in range(0, len(self.cars)):
            for new_car in self.cars[i].next_cars(other_cars=list(self.cars)):
                new_cars = list(self.cars)
                new_cars[i] = new_car
                board = Board(self.board_height, self.board_width, new_cars,
                              self.goal, previous=self)
                board.moves = str(i)

                if board.is_winner():
                    print("yeaaaaah")
                    state = board
                    winning_path = []
                    while state is not None:
                        winning_path.append(state)
                        state = state.previous
                    winning_path.reverse()
                    for board in winning_path:
                        print(board)
                        print("Move made with car:", board.moves)
                    print("steps made for win:", len(winning_path) - 1)
                    raise Win(board)

                hash0 = hash(board)
                if hash0 not in hash_table.states_checked_hash_table:
                    hash_table.states_checked_hash_table[hash0] = [board]
                    new_boards.append(board)
                elif board not in \
                        hash_table.states_checked_hash_table[hash0]:
                    new_boards.append(board)
                    hash_table.states_checked_hash_table[hash0].append(board)
        return new_boards

    def car_that_contains_position(self, position: Position):
        """
        Returns car at certain position.
        """
        for i in range(0, len(self.cars)):
            if position in self.cars[i].positions:
                return self.cars[i]
        return None


    def calculate_tree(self, goal, depth, max_depth):
        depth += 1
        if (depth > max_depth):
            return {}
        tree = {}
        for blocking_car in self.blocking_cars(goal):
            index = self.cars.index(blocking_car)
            tree[index] = {}
            possible_moves = blocking_car.real_possible_moves(self.cars, goal)
            for move in possible_moves:
                new_goal = (index, blocking_car.goal_pos_from_move(move))
                tree[index][move] = self.calculate_tree(new_goal, depth, max_depth)
                if tree[index][move] is None:
                    del tree[index][move]
            if len(tree[index]) == 0:
                tree = None
        return tree


    def a_star_count(self, admissable=False):
        value = 0
        if Board.a_star_depth == 1:
            value += self.blocking_value(self.goal)
        elif Board.a_star_depth == 2:
            tree = self.calculate_tree(self.goal, 0, 2)
            value += count_tree(tree)
        else:
            raise Exception("Depth should be 1 or 2.")

        if admissable:
            return value + self.count
        else:
            return value


    def a_star_count_easy(self):
        return len(self.blocking_cars(self.goal)) + self.count

    def blocking_value(self, goal: (int, Position)) -> int:
        blocking_cars = self.blocking_cars(goal)
        return len(blocking_cars)

    def blocking_cars(self, goal: (int, Position)) -> List[Car]:
        (index, goal_pos) = goal
        car_to_move = self.cars[index]
        if car_to_move.horizontal:
            if goal_pos.x < car_to_move.start.x:
                mega_car_start = Position.new(car_to_move.start.x - 1, car_to_move.start.y)
            else:
                mega_car_start = Position.new(car_to_move.end.x + 1, car_to_move.end.y)
        else:
            if goal_pos.y < car_to_move.start.y:
                mega_car_start = Position.new(car_to_move.start.x, car_to_move.start.y - 1)
            else:
                mega_car_start = Position.new(car_to_move.end.x, car_to_move.end.y + 1)

        mega_car = MegaCar(
            min(mega_car_start, goal_pos),
            max(mega_car_start, goal_pos)
        )
        return mega_car.no_clash_all_cars(self.cars)


    def __str__(self, *args, **kwargs):
        """
        Give color and number to cars in visualization.
        """
        board = '\n'
        for y in range(0, self.board_height):
            for x in range(0, self.board_width):
                if self.car_that_contains_position(Position.new(x, y)) is not None:
                    i = self.cars.index(
                        self.car_that_contains_position(Position.new(x, y)))
                    if i == 0:

                        board += colored(str(i).zfill(2), 'red') + ' '
                    else:
                        board += color(str(i).zfill(2), i) + ' '
                else:
                    board += 'XX '
            board += '\n'
        return board

    def __hash__(self) -> int:
        return hash(tuple(self.cars))

    def __eq__(self, other: 'Board') -> bool:
        return self.cars == other.cars


def color(text, i):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        text = fmt_str % (i % 7 + 30, text)
        text += RESET
    return text

class Win(Exception):
    """
    Raised when solution is found.
    """
    def __init__(self, board: Board):
        self.board = board

def get_nice_string(list_or_iterator):
    return "[" + ", ".join( str(x) for x in list_or_iterator) + "]"


def count_tree(tree: Dict) -> int:
    count = 0
    count += len(tree)
    save_car_moved = set([])
    for index_car, moves_dict in tree.items():
        delta_count = math.inf
        delta_car_moved = set([])
        for move, car_to_move_dict in moves_dict.items():
            delta_delta_count = 0
            for car_to_move, _ in car_to_move_dict.items():
                if car_to_move not in save_car_moved:
                    delta_delta_count += 1
                delta_car_moved.add(car_to_move)
            delta_count = min(delta_count, delta_delta_count)
        save_car_moved = save_car_moved.union(delta_car_moved)
        count += delta_count
    return count


def count_tree2(tree: Dict) -> int:
    root = CarNode(None, [4], 0, 0)
    root.children[0].children = []

    for key, value in tree.items():
        car_children = root.children[0].children
        car_children.append(CarNode(root.children[0], value, key, 1))

    for i in range(len(CarNode.depth_nodes) - 1, 0, -1):
        car_list = CarNode.depth_nodes[i]
        move_list = []
        for car in car_list:
            move_parent = car.parent
            move_value = 1
            for car in move_parent.children:
                move_value += car.value
            move_parent.value = move_value
            move_list.append(move_parent)
        for move in move_list:
            car_parent = move.parent
            min_value = math.inf
            for move_child in car_parent.children:
                min_value = min(move_child.value, min_value)
            car_parent.value = min_value
    return root.value

class CarNode:
    depth_nodes = []

    def __init__(self, parent: 'MoveNode', childrenInt: List[int], index: int, depth: int):
        self.depth = depth
        if len(CarNode.depth_nodes) < depth + 1:
            CarNode.depth_nodes.append([self])
        else:
            CarNode.depth_nodes[depth].append(self)
        self.parent = parent
        self.index = index
        self.children = []

        if type(childrenInt) is dict:
            for key, value in childrenInt.items():
                if value == '...' or value == 'possible':
                    move_node = MoveNode(self, 0)
                    move_node.value = 1
                    self.value = 1
                    if value == 'possible':
                        car_parent = move_node.parent
                        other_move_node = MoveNode(car_parent, 0)
                        other_move_node.value = 1

                        car_parent.children = [other_move_node]
                    else:
                        self.children.append(move_node)

                else:
                    move_node = MoveNode(self, key)
                    move_node.children = []
                    for k, v in value.items():
                        new_depth = self.depth + 1
                        move_node.children.append(CarNode(move_node, v, k, new_depth))
                    self.children.append(move_node)
        else:
            for i in childrenInt:
                self.children.append(MoveNode(self, i))

    def __str__(self):
        return "Car: " + str(self.index)

class MoveNode:
    def __init__(self, parent: 'CarNode', move: int):
        self.parent = parent
        self.move = move

    def __str__(self):
        return "Move: " + str(self.move)

max_depth = 10