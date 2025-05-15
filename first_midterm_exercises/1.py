from AI.searching_framework import *

class GhostOnSkates(Problem):

    def __init__(self, initial, holes, n, goal):
        super().__init__(initial, goal)
        self.n = n
        self.holes = holes

    def successor(self, state):
        successors = dict()
        movements = ["Up 1", 'Up 2', 'Up 3', 'Right 1', 'Right 2', 'Right 3']
        possible_movements = [(0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0)]

        ghost = state
        for i in range (len(movements)):
            movement = movements[i]
            possible_movement = possible_movements[i]

            new_ghost = (ghost[0] + possible_movement[0], ghost[1] + possible_movement[1])

            if new_ghost in self.holes: continue

            if not self.check_valid(new_ghost, self.holes, self.n): continue

            successors[movement] = new_ghost

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state, walls, n):
        if state in walls:
            return False
        if  0 <= state[0] < n-1 or 0 <= state[1] < n-1:
            return True
        return True

    def heuristic(self, node):
        g_x, g_y = node.state
        goalx, goaly = self.goal
        return (abs(g_x - goalx) + abs(g_y - goaly))/3


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)

    res = astar_search(problem)
    if res is None:
        print("No solution found")
    else:
        print(res.solution())