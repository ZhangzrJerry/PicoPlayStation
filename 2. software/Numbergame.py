from random import random


class Numbergame:
    def __init__(self) -> None:
        self.gamemap = [[0,0,0,0],
                        [0,-1,-1,-1],
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
        # TODO 
        pass

    def left(self):
        for i in range(0,4):
            temp = []
            for j in range(0,4):
                if(self.gamemap[i][j]>-1):
                    temp.append(self.gamemap[i][j])
            mark = 0
            while j<temp.__len__():
                # 相同元素消除&升级
                if(j!=temp.__len__()-1 and temp[j]==temp[j+1]):
                    self.gamemap[i][mark]=temp[j]+1
                    j += 2
                    mark += 1
                # 无法消除元素直接填入
                else:
                    self.gamemap[i][mark]=temp[j]
                    j += 1
                    mark += 1
            # 空格填入-1
            for j in range(mark,4):
                self.gamemap[i][j]=-1
            del temp

                


a = Numbergame()
print("init",a.gamemap)
a.left()
print("test",a.gamemap)
