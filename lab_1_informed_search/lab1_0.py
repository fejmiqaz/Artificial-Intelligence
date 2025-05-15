from AI.searching_framework import *

def valid(snake, red_apples):
    if len(snake) != len(set(snake)): # check if the snake hits itself
        return False

    for coord in snake: #check for if the snake eats red apples
        if coord in red_apples:
            return False

    #check if the snake is inside bounds
    if 0 <= snake[-1][0] < 10 and 0 <= snake[-1][1] < 10:
        return True
    return False

def move_forward(state):
    snake = state[0] # get the snake, its head and body
    snake_direction = state[1] # initial direction
    green_apples = state[2] # green apples

    movements = {'l': (-1,0), 'r': (+1,0), 'd': (0,-1), 'u': (0,+1)} # set the directions

    new_snake_head = (snake[-1][0] + movements[snake_direction][0], snake[-1][1] + movements[snake_direction][1])

    if new_snake_head in green_apples:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != new_snake_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, snake_direction, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, snake_direction, green_apples)
        return new_state

def move_left(state):
    snake = state[0]
    snake_direction = state[1]
    green_apples = state[2]

    movements = {'l': (0,-1), 'r': (0,+1), 'd': (+1,0), 'u': (-1,0)}
    new_head_positions = {'l': 'd', 'r': 'u', 'd': 'r', 'u': 'l'}
    new_head_direction = new_head_positions[snake_direction]
    new_snake_head = (snake[-1][0] + movements[snake_direction][0], snake[-1][1] + movements[snake_direction][1])

    if new_snake_head in green_apples:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != new_snake_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, new_head_direction, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, new_head_direction, green_apples)
        return new_state

def move_right(state):
    snake = state[0]
    snake_direction = state[1]
    green_apples = state[2]

    movements = {'l': (0,+1), 'r': (0,-1), 'd': (-1,0), 'u': (+1,0)}
    new_head_positions = {'l': 'u', 'r': 'd', 'd': 'l', 'u': 'r'}
    new_head_dir = new_head_positions[snake_direction]
    new_snake_head = (snake[-1][0] + movements[snake_direction][0], snake[-1][1] + movements[snake_direction][1])

    if new_snake_head in green_apples:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != new_snake_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, new_head_dir, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(new_snake_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, new_head_dir, green_apples)
        return new_state


class SnakeGame(Problem):

    def __init__(self, initial,red_apples):
        super().__init__(initial, goal=None)
        self.red_apples = red_apples


    def successor(self, state):
        successors = dict()

        move_funcs = [
            move_forward, move_right, move_left
        ]
        actions = [
            "ContinueStraight", "TurnRight", "TurnLeft"
        ]

        for i in range(len(actions)):
            new_state = move_funcs[i](state)
            if valid(new_state[0], self.red_apples):
                successors[actions[i]] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == "__main__":
    num_green_apples = int(input())
    green_apples = []
    for i in range(num_green_apples):
        values = tuple(map(int,input().split(",")))
        green_apples.append(values)

    num_red_apples = int(input())
    red_apples = []
    for i in range(num_red_apples):
        values = tuple(map(int,input().split(",")))
        red_apples.append(values)

    green_apples = tuple(green_apples)
    red_apples = tuple(red_apples)

    initial_state = (((0,9),(0,8),(0,7)), 'd',green_apples)

    snakeGame = SnakeGame(initial_state, red_apples)
    res = breadth_first_graph_search(snakeGame)

    if res is not None:
        print(res.solution())
    else:
        print([])