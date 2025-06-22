from AI.searching_framework import *

class LaserGame(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        man = state[0]
        laser = state[1]
        timer = state[2]
        barriers = state[3]
        m = state[4]
        n = state[5]

        movementsAvailable = ("Up", "Down", "Left", "Right", "Stand")
        movements = ((1,0),(-1,0),(0,1),(0,-1),(0,0))

        for i in range(len(movementsAvailable)):
            movement = movementsAvailable[i]
            movementAvailable = movements[i]

            new_man = (man[0] + movementAvailable[0], man[1] + movementAvailable[1])

            if (new_man in barriers) or (m <= new_man[0] <= 0 and n <= new_man[1] <= 0):
                continue

            new_laser = laser

            if timer == 1:
                new_laser = new_man

            if timer == 4:
                timer = 1
                if man == laser:
                    continue
            timer = timer + 1

            new_state = (new_man,new_laser,timer,barriers,m,n)
            successors[movement] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man = state[0]
        return man == self.goal


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    man = tuple(map(int, input().split(",")))
    goalPosition = tuple(map(int, input().split(",")))
    laser = tuple(map(int, input().split(",")))
    timer = int(input())
    k_num = int(input())
    barriers = []
    for i in range(k_num):
        values = tuple(map(int, input().split(",")))
        barriers.append(values)
    barriers = tuple(barriers)

    initial = (man,laser,timer,barriers,m,n)
    problem = LaserGame(initial, goalPosition)

    res = breadth_first_graph_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print("No solution")