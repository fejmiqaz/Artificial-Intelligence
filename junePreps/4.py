from AI.searching_framework import *

class BallMovement(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        balls = state[0]
        opponents = state[1]

        movements = ("UpLeft", "UpRight", "DownLeft", "DownRight", "Left", "Right")
        movements_coord = ((-1,1), (1,1), (-1,-1), (1,1), (0,-1), (0,1))

        for ball in balls:
            for i in range(len(movements)):
                movement = movements[i]
                movement_coord = movements_coord[i]

                new_ball = (ball[0] + movement_coord[0], ball[1] + movement_coord[1])

                for opponent in opponents:
                    if new_ball == opponent:
                        successors[movement] = (new_ball, opponent)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return super().goal_test(state)

    def heuristic(self, state):
        balls = self.state[0]
        opponents = self.state[1]
        min_distance = float("inf")

        for ball in balls:
            for opponent in opponents:
                distance = abs(ball[0] - opponent[0]) + abs(ball[1] - opponent[1])
                min_distance = min(min_distance, distance)

        return min_distance



if __name__ == '__main__':
    n = int(input())
    num_balls = int(input())
    ball_positions = []
    for i in range(num_balls):
        values = tuple(map(int, input().split(",")))
        ball_positions.append(values)
    ball_positions = tuple(ball_positions)
    num_opponents = int(input())
    opponents_positions = []
    for i in range(num_opponents):
        values = tuple(map(int, input().split(",")))
        opponents_positions.append(values)
    opponents_positions = tuple(opponents_positions)

    initial = (ball_positions, opponents_positions)
    problem = BallMovement(initial, opponents_positions)

    res = astar_search(problem,problem.heuristic)

    if res is not None:
        print(res.solution())
    else:
        print("No solution")
