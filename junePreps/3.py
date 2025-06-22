from AI.searching_framework import *


class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state, opponents):
        man_pos = state[0]
        ball_pos = state[1]

        if man_pos in opponents or ball_pos in opponents:
            return False

        return man_pos[0] >= 0 and man_pos[0] < 8 and \
            man_pos[1] >= 0 and man_pos[1] < 6 and \
            ball_pos[0] >= 0 and ball_pos[0] < 8 and \
            ball_pos[1] >= 0 and ball_pos[1] < 6

    def successor(self, state):
        successors = dict()

        man = state[0]
        ball = state[1]
        opponents = state[2]

        movements = ("Move man up", "Move man down", "Move man up-right", "Move man down-right")
        ball_movements = ("Push ball up", "Push ball down", "Push ball up-right", "Push ball down-right")
        possible_movements = ((1,0), (-1,0), (1,1), (-1,-1))

        for i in range(len(movements)):
            movement = movements[i]
            possible_movement = possible_movements[i]
            ball_movement = ball_movements[i]

            new_man = (man[0] + possible_movement[0], man[1] + possible_movement[1])

            if new_man == ball:
                new_ball = (ball[0] + possible_movement[0], ball[1] + possible_movement[1])
                new_state = (new_man, new_ball, opponents)

                if self.check_valid(new_state, opponents):
                    successors[ball_movement] = new_state
                else:
                    new_state = (new_man, new_ball, opponents)
                    if self.check_valid(new_state, opponents):
                        successors[movement] = new_state

        return successors

    def h(self, node):
        ball_pos = node.state[1]
        min_distance = float("inf")

        for goal_pos in self.goal:
            distance = abs(ball_pos[0] - goal_pos[0]) + abs(ball_pos[1] - goal_pos[1])
            min_distance = min(min_distance, distance)

        return min_distance


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))

    opponents = [(3, 3), (5, 4)]
    opponents = tuple(opponents)

    initial = (man_pos,ball_pos, opponents)
    goal = [(6,3),(6,2)]
    goal = tuple(goal)
    problem = Football(initial, goal)

    res = astar_search(problem, problem.h)

    if res is not None:
        print(res.solution())
    else:
        print("No solution")
