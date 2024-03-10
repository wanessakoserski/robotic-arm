from robotic_arm import RoboticArm
import random
import numpy as np
from basic.node import Node

if __name__ == "__main__":
    problem = RoboticArm()
    problem.start()
    print(problem.show(problem.root_node))
    print(problem.test_goal(Node([4, 0, 10, 20, 30, 0, 0, 0, 10, 20, 40, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0,0, 0, 0,])))

    