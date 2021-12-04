# Enemies 1
class Goomba:
    def __init__(self, x:int, y:int, dir:bool):
        self.x = x
        self.y = y
        self.dir = dir
        self.sprite = ()

    def move(self, direction: str, size: int):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        goomba_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - goomba_x_size:
            self.x = self.x + 1
        elif direction.lower() == 'left' and self.x > 0:
            # I am assuming that if it is not right it will be left
            self.x -= 1
    def collision(self, colision:bool):

            """
            if (rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and
                rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y):
                self.colision = True
            """
