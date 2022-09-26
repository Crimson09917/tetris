import pygame
from math import ceil


class Board:
    def __init__(self, dimension):
        # {"x1,y1":(r1, g1, b1), "x2,y2":(r2, g2, b2)}
        self.colourDict = {}
        self.createCellArray()
        self.dimension = dimension
        self.score = 0
        self.addCell("1000,1000", (0, 0, 0))

    def addCell(self, coords, colour):
        # coords is in form "<x>,<y>"
        # colour is a tuple
        self.colourDict[coords] = colour
        self.createCellArray()

    def addCells(self, array):
        # Array must be in form [["<x>,<y>", <colour(Tuple)>], ["<x>,<y>", <colour(Tuple)>]]
        for i in array:
            self.addCell(i[0], i[1])

    def createCellArray(self):
        coords = list(self.colourDict.keys())
        for i in range(len(coords)):
            coords[i] = coords[i].split(",")
            coords[i][0] = int(coords[i][0])
            coords[i][1] = int(coords[i][1])

        self.cellArray = coords

    def deleteCell(self, coords):
        # coords must be in form: "<x1>,<y1>"
        del self.colourDict[coords]
        self.createCellArray()

    def display(self, window):
        for i in self.cellArray:
            x = i[0]
            y = i[1]
            colour = self.colourDict[str(i[0]) + "," + str(i[1])]
            pygame.draw.rect(window, colour, (x, y, self.dimension, self.dimension))
            pygame.draw.rect(window, (100, 100, 100), (i[0], i[1], self.dimension, self.dimension), 2)

    def checkCollision(self, piece):
        for i in self.cellArray:
            for j in piece.pieceCoords:
                if j[0] == i[0] and j[1] + self.dimension == i[1]:
                    return True
                elif j[1] == 800:
                    return True
        return False

    def placePiece(self, piece):
        for i in piece.pieceCoords:
            self.colourDict[str(i[0])+","+str(i[1])] = piece.colour
        self.createCellArray()
        self.checkRows()

    def checkRows(self):
        # iterates through all items in the cellArray
        # For every y value there is a total in an array called total
        rowTotal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for cell in self.cellArray:
            index = ceil(cell[1]/self.dimension)-1
            if index == 24:
                continue
            rowTotal[index] += 1

        deleteY = False
        for i, row in enumerate(rowTotal):
            if row == 10:
                deleteY = (i+1)*self.dimension
                break
        if deleteY:
            for x in range(40, 440, 40):
                del self.colourDict[str(x)+","+str(deleteY)]
            self.createCellArray()

            # iterate through the y coords that need to be moved down (bottom to top)
            for y in range(deleteY, 0, -1*self.dimension):
                for cell in self.cellArray:
                    if cell[1] == y:
                        key = str(cell[0]) + "," + str(y)
                        newKey = str(cell[0]) + "," + str(y + self.dimension)

                        self.colourDict[newKey] = self.colourDict[key]
                        del self.colourDict[key]
            self.score += 1
            self.createCellArray()
            self.checkRows()
