from mario import Mario
from bricks import Bricks
import pyxel

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width/2, 210, True)
        self.bricks = Bricks( 0 , self.width - 32)
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
        if 255-32 >= self.mario.y:
            if self.mario.collison(Bricks) == False:
                self.mario.fall()

    def draw(self):
        pyxel.cls(0)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], colkey=12)
        # pyxel.bltm(-1, -1, 0,0, 80, 32, 16)

        pyxel.blt(self.bricks.x, self.bricks.y, self.bricks.sprite[0],
                self.bricks.sprite[1], self.bricks.sprite[2], self.bricks.sprite[3],
                self.bricks.sprite[4])

    def extras(self):
        # Mario
        pyxel.text(20, 20, "MARIO", 0)
        pyxel.text(20, 28, "00000", 0)
        # Para los coins
        pyxel.text(70, 20, str(self.coins), 0)
        # In the meantime, this is a star. I need it to be a coin
        pyxel.blt(85, 17, 0, 0, 104, 16, 16, colkey=12)
        # WORLD
        pyxel.text(120, 20, "WORLD: 1-1", 0)
        # TITLE
        pyxel.text(90, 5, "THIS IS SUPER MARIO", 0)
        # TIMER
        # meterle el countdown
        pyxel.text(200, 20, "TIMER", 0)
# blt clases. (x, y, im, u, v)
# bltm escenario