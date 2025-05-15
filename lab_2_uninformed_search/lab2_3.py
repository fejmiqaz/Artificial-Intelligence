from AI.searching_framework import *

class SmallHouse(Problem):
    def __init__(self, initial, allowed):
        super().__init__(initial, goal=None)
        self.allowed = allowed
        self.grid_size = (5,9)

    def successor(self, state):
        successors = dict()

        movements = ("Stay", "Up 1", "Up 2", "Up-right 1", "Up-right 2", "Up-left 1", "Up-left 2")
        pos_movements = ((0, 0), (0, 1), (0, 2), (1, 1),(2, 2), (-1, 1), (-2, 2))
        character = state[0]
        house = state[1]
        direction = state[2]


        for i in range(len(movements)):
            movement = movements[i]
            pos_movement = pos_movements[i]

            new_char = (character[0] + pos_movement[0], character[1] + pos_movement[1])
            new_house = self.move_house(direction, house, len(successors))


            if (new_char not in self.allowed) or (not self.in_bounds(new_char)):
                continue

            successors[movement] = (new_char, new_house[0], new_house[1])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        print(state[0], state[1])
        return state[0] == state[1]

    def heuristic(self, node):
        # state = node.state
        # character = state[0]
        # char_y = character[1]
        # if self.grid_size[0] - 1 == char_y:
        #     return 0
        # return (self.grid_size[0] - 1 - char_y) / 2
        character, house, _ = node.state
        return abs(character[0] - house[0]) + abs(character[1] - house[1])

    def move_house(self, direction, house, step):
        if step % 2 == 0:
            x, y = house
            if direction == 'right':
                if x == 4:
                    x = 3
                    direction = "left"
                else:
                    x += 1
            elif direction == 'left':
                if x == 0:
                    x = 1
                    direction = "right"
                else:
                    x -= 1
            return ((x, y), direction)
        return (house, direction)

    def in_bounds(self, state):
        print(state[0], state[1])
        return 0 <= state[0] < self.grid_size[0] and 0 <= state[1] < self.grid_size[1]



if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    character = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    house_direction = input()

    initial_state = (character, house, house_direction)

    problem = SmallHouse(initial_state, allowed)
    res = astar_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print([])
