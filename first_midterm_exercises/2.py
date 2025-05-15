import copy

from AI.searching_framework import *


class StackedPillars(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        state = [state.split(",") if stack else [] for stack in state]

        for i in range(len(state)):
            if state[i]:
                top = state[i][-1]

                for j in range(len(state)):
                    if i!=j:
                        new_state = copy.deepcopy(state)
                        new_state[j].append(new_state[i].pop())
                        successors[f"MOVE TOP BLOCK FROM PILLAR {i} TO PILLAR {j}"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == "__main__":
    pillars = input()
    pillar1 = tuple(map(int, pillars.split(";")[0].split(",")))
    pillar2 = tuple(map(int, pillars.split(";")[1].split(",")))
    pillar3 = tuple(map(int, pillars.split(";")[2].split(",")))
    initial_state = (pillar1, pillar2, pillar3)

    goals = input()
    goal1 = tuple(map(int,goals.split(";")[0].split(",")))
    goal2 = tuple(map(int, goals.split(";")[1].split(",")))
    goal3 = tuple(map(int, goals.split(";")[2].split(",")))
    goal_state = (goal1, goal2, goal3)

    print(initial_state)
    print(goal_state)

    problem = StackedPillars(initial_state, goal_state)
    # res = depth_limited_search(problem)
    # if res is None:
    #     print("No solution found")
    # else:
    #     print(res.solution())