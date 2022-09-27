from random import random


class Numbergame:
    def __init__(self) -> None:
        self.gamemap = [[2,0,2,2],
                        [2,0,-1,-1],
                        [-1,-1,-1,-1],
                        [-1,-1,-1,-1]]
        self.gamenum = [2,4,8,16,32,64,128,256,512,1024,2048]
        pass

    def random_create(self):
        temp = []
        # 把空元素放入列表
        for i in range(0,4):
            for j in range(0,4):
                if self.gamemap[i][j] == -1:
                    temp.append([i,j])
        # 抽取任一空元素
        mark = temp[int(random()*temp.__len__())]
        num = 0 if random() < 0.75 else 1
        self.gamemap[mark[0]][mark[1]] = num
        pass


    def if_win(self):
        if self.gamenum.__len__()-1 in self.gamemap:
            return True
        return False

    def if_end(self):
        for i in range(0,4):
            for j in range(0,4):
                # 仍有空元素
                if self.gamemap[i][j] == -1:
                    return True
                # 有可消除元素
                if self.limit(i-1,j) and self.gamemap[i][j]==self.gamemap[i-1][j]:
                    return True
                if self.limit(i+1,j) and self.gamemap[i][j]==self.gamemap[i+1][j]:
                    return True
                if self.limit(i,j-1) and self.gamemap[i][j]==self.gamemap[i][j-1]:
                    return True
                if self.limit(i,j+1) and self.gamemap[i][j]==self.gamemap[i][j+1]:
                    return True
        return False

    def limit(x,y):
        if x < 0:
            return False
        if x > 3:
            return False
        if y < 0:
            return False
        if y > 3:
            return False
        return True

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

    def right(self):
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

    def up(self):
        # 列遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(0,4):
                if self.gamemap[j][i] > -1:
                    if mark > -1:
                        if temp[mark] == self.gamemap[j][i]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.gamemap[j][i])
            # 为列填入元素
            while temp.__len__()<4:
                temp.append(-1)
            for j in range(0,4):
                self.gamemap[j][i] = temp[j]
            del temp
        pass

    def down(self):
        # 列遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(3,-1,-1):
                if self.gamemap[j][i] > -1:
                    if mark > -1:
                        if temp[mark] == self.gamemap[j][i]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.gamemap[j][i])
            # 为列填入元素
            while temp.__len__()<4:
                temp.append(-1)
            for j in range(3,-1,-1):
                self.gamemap[j][i] = temp[3-j]
            del temp
        pass
        


                


a = Numbergame()
print("init",a.gamemap)
a.random_create()
print("test",a.gamemap)
