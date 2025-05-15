from AI.searching_framework import *

def is_within_bounds(coordinate):
    flag = False
    if 0 <= coordinate[0] < 8 and 0 <= coordinate[1] < 6:
        flag = True
    return flag

def adjacent_squares(square):
    cells = set()
    for i in range(-1,2):
        for j in range(-1,2):
            cells.add((square[0] + i, square[1] + j))
    return cells

def state_check(state,opponents):
    man = state[0]
    ball = state[1]
    if man in opponents or ball in opponents:
        return False
    if ball in adjacent_squares(opponents[0]) or ball in adjacent_squares(opponents[1]):
        return False
    return is_within_bounds(man) and is_within_bounds(ball)

class FootballGame(Problem):
    def __init__(self, initial_state, opponents, goal):
        super().__init__(initial_state,goal=None)
        self.opponents = opponents
        self.goal = goal

    def successor(self, state):
        successors = dict()

        movements = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        noBallMovements = (
            "Move man up", "Move man up-right", "Move man right",
            "Move man down-right", "Move man down",
        )
        ballMovements = (
            "Push ball up", "Push ball up-right", "Push ball right",
            "Push ball down-right", "Push ball down"
        )


        man = state[0]
        ball = state[1]

        num_of_movements = int(len(movements))

        for i in range(num_of_movements):
            movement = movements[i]
            ballMovement = ballMovements[i]
            noBallMovement = noBallMovements[i]

            new_coordinate = (man[0] + movement[0], man[1] + movement[1])

            if new_coordinate == ball:
                new_ball = (new_coordinate[0] + movement[0], new_coordinate[1] + movement[1])
                new_state = (new_coordinate, new_ball, opponents)
                if state_check(new_state, self.opponents):
                    successors[ballMovement] = new_state
            else:
                new_state = (new_coordinate, ball, opponents)
                if state_check(new_state, self.opponents):
                    successors[noBallMovement] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal


if __name__ == "__main__":
    man = tuple(map(int,input().split(",")))
    ball = tuple(map(int,input().split(",")))

    opponents = ((3,3),(5,4))
    goals = ((7,2),(7,3))

    initial = (man,ball)

    football_game = FootballGame(initial,opponents, goals)

    res = breadth_first_graph_search(football_game)
    if res is None:
        print("No Solution!")
    else:
        print(res.solution())