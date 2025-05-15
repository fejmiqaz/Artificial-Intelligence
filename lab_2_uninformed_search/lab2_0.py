from AI.searching_framework import *

class Lab_2(Problem):

    def __init__(self, initial, obstacles,grid_size):
        super().__init__(initial, goal=initial[1])
        self.grid_size = grid_size
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        movements = ('Right', 'Left', 'Down', 'Up', 'Right 2', 'Right 3')
        possible_movements = ((1, 0),(-1, 0), (0, -1), (0, 1), (2, 0), (3, 0))

        man = state[0]
        house = state[1]

        for i in range(len(movements)):
            movement = movements[i]
            pm = possible_movements[i]

            new_man = (man[0] + pm[0], man[1] + pm[1])

            if not self.in_bounds(new_man) or new_man in self.obstacles:
                continue

            if movement == 'Right':
                continue

            if movement == "Right 2":
                if ((man[0] + 1, man[1]) in self.obstacles) or (new_man in self.obstacles):
                    continue

            if movement == "Right 3":
                if ((man[0] + 1, man[1]) in self.obstacles) or ((man[0] + 2 , man[1]) in self.obstacles) or (new_man in self.obstacles):
                    continue

            successors[movement] = (new_man, house, self.obstacles)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal

    def heuristic(self,node):
        x_man, y_man = node.state[0]
        x_house, y_house = node.state[1]
        value = 0
        if x_man < x_house:
            distance = x_house - x_man
            if distance == 1:
                return 2
            elif distance % 3 == 0:
                value += distance // 3
            else:
                value += (distance // 3) + 1

        if x_man > x_house:
            value += x_man - x_house

        value += abs(y_man - y_house)

        return value


    def in_bounds(self, state):
        if 0 <= state[0] < self.grid_size and 0 <= state[1] < self.grid_size:
            return True
        else:
            return False

if __name__ == '__main__':
    grid_size = int(input())
    num_walls = int(input())
    obstacles = []
    for i in range(num_walls):
        obstacles.append(tuple(map(int, input().split(","))))
    obstacles = tuple(obstacles)
    man = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    initial_state = (man, house)

    game = Lab_2(initial_state,obstacles, grid_size)

    res = astar_search(game)
    if res is None:
        print("No Solution!")
    else:
        print(res.solution())
