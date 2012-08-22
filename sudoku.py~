#Sudoku problem
from math import sqrt
from random import shuffle

class Sudoku:
    def __init__(self, size = 4):
        self.size = size
        self.table = [[-2 for i in range(size)] for j in range(size)]
        self.forbiddenDict = {}
        for i in range(size):
            for j in range(size):
                self.forbiddenDict[(i,j)] = []

    def CreateValidTable(self):
        pos = 0
        if self.CalcCellValue(pos):
            return True
        return False

    def CalcCellValue(self, pos):
        xIndex = pos % self.size
        yIndex = pos // self.size

        validList = self.GetValidValue(pos)
        shuffle(validList)

        while(True):
            if len(validList) == 0:
                break
            self.table[yIndex][xIndex] = validList.pop()    
            if pos == self.size**2-1 or self.CalcCellValue(pos + 1):
                return True

        self.table[yIndex][xIndex] = -1
        return False
            

    def GetValidValue(self, pos):
        valid = [i+1 for i in range(self.size)]
        #valid = self.CheckForbiddenDict(valid, pos)
        valid = self.CheckRowColumn(valid, pos)
        valid = self.CheckChildTable(valid, pos)
        return valid

    def CheckForbiddenDict(self, valid, pos):
        xIndex = pos % self.size
        yIndex = pos // self.size

        for val in self.forbiddenDict[(yIndex, xIndex)]:
            if val in valid:
                valid.remove(val)
        return valid

    def CheckRowColumn(self, valid, pos):
        xIndex = pos % self.size
        yIndex = pos // self.size

        for val in self.table[yIndex]:
            if val in valid:
                valid.remove(val)
        for val in [row[xIndex] for row in self.table]:
            if val in valid:
                valid.remove(val)
        return valid

    def CheckChildTable(self, valid, pos):
        xIndex = pos % self.size
        yIndex = pos // self.size
        childTableOriginX = int((xIndex // sqrt(self.size)) * sqrt(self.size))
        childTableOriginY = int((yIndex // sqrt(self.size)) * sqrt(self.size))

        for x in range(childTableOriginX, childTableOriginX+int(sqrt(self.size))):
            for y in range(childTableOriginY, childTableOriginY+int(sqrt(self.size))):
                if self.table[y][x] in valid:
                    valid.remove(self.table[y][x])
        return valid

    def PrintSudokuTable(self):
        for row in self.table:
            print(row)        
        

if __name__ == '__main__':
    tb = Sudoku(9)

    result = tb.CreateValidTable()
    print(result)
    if result:
        tb.PrintSudokuTable()
