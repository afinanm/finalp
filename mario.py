import time
import math
from typing import Union, Any

import goomba
from goomba import Goomba

"""
def collision(character1, character2, colision: bool):
    if (character1.x < character2.x + character2.width and character1.x + character1.width > character2.x and
        character1.y < character2.y + character2.height and character1.height + character1.y > character2.y):
        colision = True
"""

class Mario:
    """ This class stores all the information needed for Mario"""

    def __init__(self, x: int, y: int, dir: bool):
        """ This method creates the Mario object
        @param x the starting x of Mario
        @param y the starting y of Mario
        @param dir a boolean to store the initial direction of Mario.
                True is facing right, False is facing left"""
        self.x = x
        self.y = y
        self.direction = dir
        # Here we are assuming Mario will be always placed at the first
        # bank at first position and it will have a 16x16 size
        self.sprite = (0, 0, 48, 16, 16)
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3
        self.is_jumping = False
        self.is_falling = False

    def move(self, direction: str, size: int):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            self.x = self.x + 1
        elif direction.lower() == 'left' and self.x > 0:
            # I am assuming that if it is not right it will be left
            self.x -= 1

    """
    def jump(self, jump: bool):
        mario_x_size = self.sprite[3]
        if jump:
            self.y -= 1
            self.x += 1
    """
    def jump(self, is_jumping: bool):
        if is_jumping == True and self.is_falling == False:
            self.is_jumping = True
            self.y -= 6

    def gravity(self):
        if self.is_jumping == True and self.is_falling == False:
            self.is_falling = True
            # this does work but it won't first execute jumping and later
            # execute gravity, it executes both at the same time
            # and Mario won't move if both values of +y and -y are equal

    def fall(self):
        if self.is_jumping == True and self.is_falling == True:
            self.y += 1


    def collison(self, other):
        width1 = self.sprite[4]
        height1 = self.sprite[3]
        width2 = other.sprite[4]
        height2 = other.sprite[3]

        x_collison = (math.fabs(self.x - other.x)*2) < (width1 + width2)
        y_collison = (math.fabs(self.y - other.y)*2) < (height1 + height2)
        return (x_collison and y_collison)

    """
    def collision(self, other):
        width1 = self.sprite[4]
        height1 = self.sprite[3]
        width2 = other.sprite[4]
        height2 = other.sprite[3]

        if (self.x < character2.x + width2 and self.x + width1 > character2.x and
                self.y < character2.y + height2 and height1 + self.y > character2.y):
            colision = True

        return colision
    """