from mario import Mario
from bricks import Bricks
import pyxel
import time

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int, time: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at 0 in x and at y = 200
        # facing right
        self.mario = Mario(0, 206, True)
        self.bricks = Bricks(0, self.height - 16)
        # EXTRAS
        self.score = 0
        self.coins = 00
        self.time = time.time()
        self.initial_time = time
        self.lives = self.mario.lives
        self.pipes = Pipes(200, self.height - 64)
        #self.floor = bricks

        # self.floor1 = self.floor()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_UP):
            self.mario.jump(True)
            self.mario.gravity()

        if 255 - 32 >= self.mario.y and self.mario.collison(self.bricks) == False:
            self.mario.fall()

    def extras(self):
        #TITLE
        pyxel.text(90,15, "THIS IS SUPER MARIO", 0)
        #Mario
        pyxel.text(20,30, "MARIO", 0)
        pyxel.text(20,38, "00000", 0)
        #COINS
        pyxel.text(70,30, "x"+str(self.coins), 0)
        # Drawing the coin
        pyxel.blt(78, 27, 0, 48, 104, 16, 16, colkey = 12)
        #LIVES
        pyxel.text(100, 30, "x"+ str(self.lives), 0)
        # Drawing the lives
        pyxel.blt(108, 26, 0, 0,120, 16,16, colkey = 12)
        # WORLD
        pyxel.text(140,30,"WORLD: 1-1", 0)
        #TIMER
        pyxel.text(200,30, "TIME", 0)
        self.remaining_time = self.initial_time - (int(time.time() - self.initial_time))
        pyxel.text(200, 38, str(self.remaining_time), 0)

    def draw(self):
        pyxel.cls(6)
        self.extras()
        # self.attempt_floor()
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4],colkey=12)

        # DRAWING THE FLOOR
        for i in range(self.width // 10):
            pyxel.blt(i*16, self.bricks.y, self.bricks.sprite[0],
                  self.bricks.sprite[1], self.bricks.sprite[2], self.bricks.sprite[3],
                  self.bricks.sprite[4],colkey=12)
        for i in range(self.width // 10):
            pyxel.blt(i*16, self.height - 32, self.bricks.sprite[0],
                  self.bricks.sprite[1], self.bricks.sprite[2], self.bricks.sprite[3],
                  self.bricks.sprite[4],colkey=12)

        #ATTEMPT: DRAWING A PIPE:
        pyxel.blt(self.pipes.x, self.pipes.y, self.pipes.sprite[0],
                  self.pipes.sprite[1], self.pipes.sprite[2], self.pipes.sprite[3],
                  self.pipes.sprite[4], colkey=12)

        # for loop
        #pyxel.bltm(-1, -1, 0, self.mario.x, 80, 32, 16) # Tile maps


    def floor(self):
        bricks = []
        for i in range(20):
            bs = Bricks(i*16, 255)
            bricks.append(bs)
        return bricks

    # def attempt_floor(self):
        # for bs in self.floor():




# blt clases. (x, y, im, u, v)
# bltm tilemap