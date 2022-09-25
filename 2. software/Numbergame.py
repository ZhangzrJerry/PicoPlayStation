from random import random


class Numbergame:
    def __init__(self) -> None:
        self.gamemap = [[-1,-1,-1,-1],
                        [-1,-1,-1,-1],
                        [-1,-1,-1,-1],
                        [-1,-1,-1,-1]]
        self.gamenum = [2,4,8,16,32,64,128,256,512,1024,2048]
        pass

    def random_create(self):
        x = int(4*random())
        y = int(4*random())
        num = self.gamenum[0] if random() < 0.75 else self.gamenum[1]
        return x,y,num

    def if_win(self):
        if self.gamenum.__len__() in self.gamemap:
            return True
        return False

    def if_end(self):
        pass

    def left(self):
        for i in range(0,4):
            temp = []
            for j in range(0,4):
                if(self.gamemap[i][j]>-1):
                    temp.append(self.gamemap[i][j])
            mark = 0
            for j in range(0,temp.__len__()-1):
                if(temp[j]==temp[j+1]):
                    self.gamemap[i][mark]=temp[j]+1
            for j in range(mark,4):
                self.gamemap[i][j]=-1
            del temp
                