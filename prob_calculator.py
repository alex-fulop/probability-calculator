import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for ball in balls.keys():
            for _ in range(balls.get(ball)):
                self.contents.append(ball)

    def draw(self, number):
        if number >= len(self.contents):
            balls_removed = self.contents
            self.contents = []
        else:
            balls_removed = self.remove_balls(number)
        return balls_removed

    def remove_balls(self, number):
        balls_removed = list()
        for _ in range(number):
            index = random.randint(0, len(self.contents) - 1)
            balls_removed.append(self.contents.pop(index))
        return balls_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_balls_contents = to_list(expected_balls)
        extractions = hat_copy.draw(num_balls_drawn)
        condition = check_condition(expected_balls_contents, extractions)
        if condition:
            success += 1

    return success / num_experiments


def check_condition(expected_balls_contents, extractions):
    condition = True
    for ball in expected_balls_contents:
        if ball in extractions:
            extractions.remove(ball)
        else:
            condition = False
    return condition


def to_list(expected_balls):
    expected_balls_contents = list()
    for ball, number in expected_balls.items():
        expected_balls_contents = expected_balls_contents + [ball] * number
    return expected_balls_contents
