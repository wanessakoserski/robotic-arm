import sys
import random
import numpy as np

from basic.node import Node

class RoboticArm:
    def __init__(self, number_of_positions=8, number_of_boxes=6):
        self.initial_arm_position = 4
        self.space_arm_info = 2
        self.boxes_per_position = 3
        self.number_of_boxes = number_of_boxes
        self.number_of_positons = number_of_positions

        self.list_size = (number_of_positions * self.boxes_per_position) + self.space_arm_info

        self.boxes = self.generate_random_boxes(number_of_boxes)
        self.boxes_positions = self.draw_positions_boxes(number_of_positions, number_of_boxes)


    def draw_positions_boxes(self, number_of_positions, number_of_boxes):
        positions = list(range(1, number_of_positions + 1))
        draw_positions = random.sample(positions, number_of_boxes)
    
        return draw_positions


    def generate_random_boxes(self, number_of_boxes):
        return np.array([random.randint(1, 5) * 10 for _ in range(number_of_boxes)])


    def start(self):
        self.list_positions = np.full(self.list_size, 0)

        # insert standard information about the arm 
        self.list_positions[0] = self.initial_arm_position

        # insert boxes
        for i in range(len(self.boxes_positions)):
            insert_index = (self.boxes_positions[i] * self.boxes_per_position) + (self.space_arm_info - 1) 
            self.list_positions[insert_index] = self.boxes[i]
    
        self.root_node = Node(self.list_positions)
        return self.root_node
    

    def test_goal(self, node):
        expected_result = self.number_of_boxes / self.boxes_per_position
        current_result = 0

        for i in range(self.number_of_positons):
            index = (i * self.boxes_per_position) + self.space_arm_info

            current_positions = []
            for position in range(self.boxes_per_position):
                current_positions.append(node.state[index + position])

            if (self.check_boxes(current_positions)):
                current_result += 1

        return expected_result == current_result


    def check_boxes(self, boxes):
        # the test considers that the number of boxes is divisible by 3 (that is, in the end there will always be 3 boxes stacked) 
        # and the top box must be the same weight or less heavy than the bottom one
        print(boxes)
        if (0 in boxes):
            return False
        elif (boxes[0] > boxes[1]):
            return False
        elif (boxes[1] > boxes[2]):
            return False
        
        return True
    

    def show(self, node):
        state = node.state

        final_state = ""
        for i in range(self.space_arm_info, self.list_size):
            final_state += str(state[i]) + " " 
            if ((i - 1) % 3 == 0):
                final_state += "\n"

        return final_state


    