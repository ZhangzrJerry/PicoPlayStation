import Numbergame
a = Numbergame.Numbergame()
print(a.gamemap)
a.gamemap[0][0] = 1
a.gamemap[0][1] = 1
a.left()
print(a.gamemap)
