from random import random


class Numbergame():
    def __init__(self) -> None:
        self.__gamemap = [[-1,-1,-1,-1],
                        [-1,-1,-1,-1],
                        [-1,-1,-1,-1],
                        [-1,-1,-1,-1]]
        self.__gamenum = [2,4,8,16,32,64,128,256,512,1024,2048]
        self.random_create()
        self.random_create()
        pass

    def random_create(self):
        temp = []
        # 把空元素放入列表
        for i in range(0,4):
            for j in range(0,4):
                if self.__gamemap[i][j] == -1:
                    temp.append([i,j])
        mark = int(random()*temp.__len__())
        if temp.__len__() <= mark:
            return
        # 抽取任一空元素
        mark = temp[mark]
        num = 0 if random() < 0.75 else 1
        self.__gamemap[mark[0]][mark[1]] = num
        pass


    def if_win(self):
        if self.__gamenum.__len__()-1 in self.__gamemap:
            return True
        return False

    def if_end(self):
        for i in range(0,4):
            for j in range(0,4):
                # 仍有空元素
                if self.__gamemap[i][j] == -1:
                    return False
                # 有可消除元素
                if self.__limit(i-1,j) and self.__gamemap[i][j]==self.__gamemap[i-1][j]:
                    return False
                if self.__limit(i+1,j) and self.__gamemap[i][j]==self.__gamemap[i+1][j]:
                    return False
                if self.__limit(i,j-1) and self.__gamemap[i][j]==self.__gamemap[i][j-1]:
                    return False
                if self.__limit(i,j+1) and self.__gamemap[i][j]==self.__gamemap[i][j+1]:
                    return False
        return True

    def __limit(self,x,y):
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
                if self.__gamemap[i][j] > -1:
                    if mark > -1:
                        if temp[mark] == self.__gamemap[i][j]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.__gamemap[i][j])
            # 为行填入元素
            while temp.__len__()<4:
                temp.append(-1)
            self.__gamemap[i] = temp
            del temp
        pass

    def right(self):
        # 行遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(3,-1,-1):
                if self.__gamemap[i][j] > -1:
                    if mark > -1:
                        if temp[mark] == self.__gamemap[i][j]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.__gamemap[i][j])
            # 为行填入元素
            while temp.__len__()<4:
                temp.append(-1)
            temp.reverse()
            self.__gamemap[i] = temp
            del temp
        pass

    def up(self):
        # 列遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(0,4):
                if self.__gamemap[j][i] > -1:
                    if mark > -1:
                        if temp[mark] == self.__gamemap[j][i]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.__gamemap[j][i])
            # 为列填入元素
            while temp.__len__()<4:
                temp.append(-1)
            for j in range(0,4):
                self.__gamemap[j][i] = temp[j]
            del temp
        pass

    def down(self):
        # 列遍历
        for i in range(0,4):
            temp = []
            mark = -1
            # 行元素遍历
            for j in range(3,-1,-1):
                if self.__gamemap[j][i] > -1:
                    if mark > -1:
                        if temp[mark] == self.__gamemap[j][i]:
                            temp[mark] = temp[mark] + 1
                            continue
                    mark += 1
                    temp.append(self.__gamemap[j][i])
            # 为列填入元素
            while temp.__len__()<4:
                temp.append(-1)
            for j in range(3,-1,-1):
                self.__gamemap[j][i] = temp[3-j]
            del temp
        pass

    def show(self):
        return self.__gamemap

    def length(self):
        return self.__gamenum.__len__()

    pass

