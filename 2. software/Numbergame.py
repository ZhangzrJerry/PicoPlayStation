from random import random


class Numbergame:
    def __init__(self) -> None:
        self.gamemap = [[2,0,2,2],
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
        # 行遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(0,4):
                if self.gamemap[i][j] > -1:
                    if mark > -1:
                        if temp[mark] == self.gamemap[i][j]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.gamemap[i][j])
            # 为行填入元素
            while temp.__len__()<4:
                temp.append(-1)
            self.gamemap[i] = temp
            del temp
        pass

    def left(self):
        # 行遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(3,-1,-1):
                if self.gamemap[i][j] > -1:
                    if mark > -1:
                        if temp[mark] == self.gamemap[i][j]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.gamemap[i][j])
            # 为行填入元素
            while temp.__len__()<4:
                temp.append(-1)
            temp.reverse()
            self.gamemap[i] = temp
            del temp
        pass



                


a = Numbergame()
print("init",a.gamemap)
a.left()
print("test",a.gamemap)
