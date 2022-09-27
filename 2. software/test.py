from Numbergame import Numbergame
game = Numbergame()
while 1:
    print(game.show())
    game.playing()
    n = input()
    if n=='left':
        game.left()
    if n=='right':
        game.right()
    if n=='up':
        game.up()
    if n=='down':
        game.down()
