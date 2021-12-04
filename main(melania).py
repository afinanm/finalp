from board import Board
import pyxel

board = Board(255,255, 10)

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(board.width, board.height, caption="This is super Mario")
# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("assets/pyxel_resource.pyxres")
# pyxel.load("assets/pyxel_resource.pyxres")
# Loading a 16x16 spaceship at bank 1 in (17,0)
# pyxel.image(2).load(17, 0, "assets/player.png")
# To start the game2 we invoke the run method with the update and draw functions
pyxel.run(board.update, board.draw)

# TEST AVISAME SI ESTO TE APARECE.
