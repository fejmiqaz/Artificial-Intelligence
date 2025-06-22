""""
MxN board
a man who can move up, down, left, right, stand (the position is read from the input)
needs to reach the target position (read from the input)
laser (the position is read from the input)
timer (from 1-5 is read from the input)
platforms on which the man is allowed to move (the number of platforms and the positions are read from the input)

when the timer = 2 the laser should come to the same position as the man
when the timer = 5 it should return to 1 and the man should be brought to the same row or column as the laser

"""

from AI.searching_framework import *


class LaserGame(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        m = state[0]
        n = state[1]
        man = state[2]
        laser = state[3]
        timer = state[4]
        platforms = state[5]

        movePositions = ("Up", "Down", "Left", "Right", "Stand")
        movingPositions = ((-1,0),(1,0),(0,-1),(0,1), (0,0))

        for i in range(len(movePositions)):
            position = movePositions[i]
            movingPosition = movingPositions[i]

            new_man = (man[0] + movingPosition[0], man[1] + movingPosition[1])

            if new_man not in platforms or new_man[0] < 0 or new_man[0] >= m or new_man[1] < 0 or new_man[1] >= n:
                continue

            new_laser = laser

            if timer == 2:
                new_laser = new_man

            if timer == 5:
                timer = 1
                new_man = new_laser

            timer = timer + 1

            new_state = (m,n,new_man,new_laser,timer, platforms)
            successors[position] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_pos = state[2]
        return man_pos == self.goal


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    man = tuple(map(int,input().split(",")))
    goalPositions = tuple(map(int,input().split(",")))
    laser = tuple(map(int,input().split(",")))
    timer = int(input())
    platforms_num = int(input())
    platforms = []
    for i in range(platforms_num):
        values = tuple(map(int, input().split(",")))
        platforms.append(values)
    platforms = tuple(platforms)

    initial_state = (m,n,man,laser,timer,platforms)

    problem = LaserGame(initial_state, goalPositions)

    res = breadth_first_graph_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print("No solution")