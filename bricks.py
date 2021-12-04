class Bricks:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = [0, 0,16,16,16]

    def move(self):
        self.y -= 1

