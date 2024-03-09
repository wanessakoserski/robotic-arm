import sys
import random
import numpy as np

class RoboticArm:
    def __init__(self, number_of_positions=8, number_of_boxes=6):
        self.initial_arm_position = 4
        self.space_arm_info = 2
        self.boxes_per_position = 3

        self.list_size = (number_of_positions * self.boxes_per_position) + self.space_arm_info

        self.boxes = self.generate_random_boxes(number_of_boxes)
        self.boxes_positions = self.draw_positions_boxes(number_of_positions, number_of_boxes)


    def start(self):
        self.list_positions = np.full(self.list_size, 0)

        # insert standard information about the arm 
        self.list_positions[0] = self.initial_arm_position

        # insert boxes
        for i in range(len(self.boxes_positions)):
            insert_index = (self.boxes_positions[i] * self.boxes_per_position) + (self.space_arm_info - 1) 
            self.list_positions[insert_index] = self.boxes[i]
    
        return self.list_positions
    

    def show(self):
        for i in range(2, self.list_size):
            print(self.list_positions[i], end=" ")
            if ((i - 1) % 3 == 0):
                print()


    def draw_positions_boxes(self, number_of_positions, number_of_boxes):
        positions = list(range(1, number_of_positions + 1))
        draw_positions = random.sample(positions, number_of_boxes)
    
        return draw_positions


    def generate_random_boxes(self, number_of_boxes):
        return np.array([random.randint(1, 5) * 10 for _ in range(number_of_boxes)])