from AI.searching_framework import *


# from utils import *
# from uninformed_search import *
# from informed_search import *

class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes
        self.number_of_balls = 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ...

    def successor(self, state):
        successors = dict()

        man = state

        movements = ["Up", "Right"]
        pos_movements = [(0,1), (1,0)]

        for i in range(len(movements)):
            movement = movements[i]
            pos_movement = pos_movements[i]

            new_man = (man[0] + pos_movement[0], man[1] + pos_movement[1])

            if not self.check_validity(new_man, self.boxes, self.n):
                continue

            self.number_of_balls += 1
            successors[movement] = (new_man, self.n, self.boxes)
        return successors

    def check_validity(self, man, boxes, n):
        if not ((0 <= man[0] < n) and (0 <= man[1] < n)): return False

        if man in boxes: return False

        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx == 0 and dy == 0: continue
                adjacent = (man[0] + dx, man[1] + dy)
                if adjacent in boxes: return True

        return True

if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    problem = Boxes(man_pos, n, boxes)

    res = breadth_first_graph_search(problem)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")