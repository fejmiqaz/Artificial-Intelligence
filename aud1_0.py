from searching_framework import *
from searching_framework.uninformed_search import breadth_first_graph_search

class Explorer(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8,6]

    def successor(self, state):
        man_x = state[0]
        man_y = state[1]

        obstacle1 = list(state[2])
        obstacle2 = list(state[3])

        successors = dict()

        if obstacle1[2] == 1: # up
            if obstacle1[1] == self.grid_size[1] - 1:
                obstacle1[2] = -1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else: # down
            if obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1

        if obstacle2[2] == 1: # up
            if obstacle2[1] == self.grid_size[1] - 1:
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else: # down
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [(obstacle1[0], obstacle2[1]), (obstacle2[0], obstacle2[1])]

        # right, x=x+1
        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:
            successors["Right"] = (man_x + 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                   (obstacle2[0], obstacle2[1], obstacle2[2]))

        #left
        if man_x - 1 > self.grid_size[0] and (man_x - 1, man_y) not in obstacles:
            successors["Left"] = (man_x - 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                  obstacle2[0], (obstacle2[1], obstacle2[2]))

        #up
        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successors["Up"] = (man_x, man_y + 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                obstacle2[0], (obstacle2[1], obstacle2[2]))

        #down
        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                 obstacle2[0], (obstacle2[1], obstacle2[2]))

        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        #(g0,g1)
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == '__main__':
    goal_state = tuple()
    for i in range(2):
        value = int(input())
        goal_state += (value,)
    initial_state = tuple()
    for i in range(2):
        value = int(input())
        initial_state += (value,)
    obstacle1 = tuple()
    for i in range(3):
        values = int(input())
        obstacle1 += (values,)
    obstacle2 = tuple()
    for i in range(3):
        values = int(input())
        obstacle2 += (values,)
    explorer = Explorer((initial_state[0], initial_state[1], obstacle1, obstacle2), goal_state)

    print(breadth_first_graph_search(explorer).solution())