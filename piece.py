import pygame


def setType():
    from random import randint
    pieceList = ["t", "o", "i", "l", "j", "s", "z"]
    return pieceList[randint(0, 6)]


class Piece:
    def __init__(self, window, board, dimension: int, pieceType, initialCoords: list, walls: list):
        if not pieceType:
            self.pieceType = setType()
        else:
            self.pieceType = pieceType

        self.board = board
        self.dimension = dimension
        self.rotation = -1
        self.placeCoords = initialCoords
        self.walls = walls
        self.window = window
        self.colour = self.getColour()

        self.pieceCoords = False
        self.rotate()

    def getColour(self):
        colour = (255, 255, 255)
        if self.pieceType == "t":
            colour = (20, 20, 200)
        elif self.pieceType == "i":
            colour = (200, 150, 0)
        elif self.pieceType == "o":
            colour = (255, 50, 50)
        elif self.pieceType == "l":
            colour = (0, 175, 0)
        elif self.pieceType == "j":
            colour = (150, 0, 150)
        elif self.pieceType == "s":
            colour = (255, 255, 0)
        elif self.pieceType == "z":
            colour = (0, 175, 175)
        return colour

    def verifyPixels(self, coordsList):
        for coord in coordsList:
            if coord[0] < self.walls[0] or coord[0] >= self.walls[2]:
                return False
            for cell in self.board.cellArray:
                if coord[0] == cell[0] and coord[1] == cell[1]:
                    return False
        return True

    def rotate(self):
        if self.pieceType == "o":
            newCoords = [[0, 0], [1, 0], [0, 1], [1, 1]]
            newRotation = 0
        if self.pieceType == "t":
            if self.rotation == 0:
                newCoords = [[0, 0], [0, 1], [1, 1], [0, 2]]
                newRotation = self.rotation + 1
            elif self.rotation == 1:
                newCoords = [[0, 0], [1, 0], [2, 0], [1, 1]]
                newRotation = self.rotation + 1
            elif self.rotation == 2:
                newCoords = [[0, 1], [1, 0], [1, 1], [1, 2]]
                newRotation = self.rotation + 1
            else:
                newCoords = [[1, 0], [0, 1], [1, 1], [2, 1]]
                newRotation = 0

        elif self.pieceType == "i":
            if self.rotation == 0:
                newCoords = [[0, 0], [1, 0], [2, 0], [3, 0]]
                newRotation = self.rotation + 1
            else:
                newCoords = [[0, 0], [0, 1], [0, 2], [0, 3]]
                newRotation = 0

        elif self.pieceType == "l":
            if self.rotation == 0:
                newCoords = [[0, 0], [1, 0], [2, 0], [0, 1]]
                newRotation = self.rotation + 1
            elif self.rotation == 1:
                newCoords = [[0, 0], [1, 0], [1, 1], [1, 2]]
                newRotation = self.rotation + 1
            elif self.rotation == 2:
                newCoords = [[0, 1], [1, 1], [2, 1], [2, 0]]
                newRotation = self.rotation + 1
            else:
                newCoords = [[0, 0], [0, 1], [0, 2], [1, 2]]
                newRotation = 0

        elif self.pieceType == "j":
            if self.rotation == 0:
                newCoords = [[0, 0], [0, 1], [1, 1], [2, 1]]
                newRotation = self.rotation + 1
            elif self.rotation == 1:
                newCoords = [[0, 0], [1, 0], [0, 1], [0, 2]]
                newRotation = self.rotation + 1
            elif self.rotation == 2:
                newCoords = [[0, 0], [1, 0], [2, 0], [2, 1]]
                newRotation = self.rotation + 1
            else:
                newCoords = [[1, 0], [1, 1], [1, 2], [0, 2]]
                newRotation = 0

        elif self.pieceType == "s":
            if self.rotation == 0:
                newCoords = [[0, 0], [0, 1], [1, 1], [1, 2]]
                newRotation = self.rotation + 1
            else:
                newCoords = [[1, 0], [2, 0], [0, 1], [1, 1]]
                newRotation = 0

        elif self.pieceType == "z":
            if self.rotation == 0:
                newCoords = [[1, 0], [1, 1], [0, 1], [0, 2]]
                newRotation = self.rotation + 1

            else:
                newCoords = [[0, 0], [1, 0], [1, 1], [2, 1]]
                newRotation = 0

        newPixels = []
        for i in newCoords:
            x = i[0] * self.dimension + self.placeCoords[0]
            y = i[1] * self.dimension + self.placeCoords[1]
            newPixels.append([x, y])

        if self.verifyPixels(newPixels):
            self.pieceCoords = newPixels
            self.placeCoords = self.pieceCoords[0]
            self.rotation = newRotation
            self.placePiece()

    def move(self, direction):
        newCoords = []
        for i in self.pieceCoords:
            if direction == "RIGHT":
                newCoords.append([i[0] + self.dimension, i[1]])
            elif direction == "LEFT":
                newCoords.append([i[0] - self.dimension, i[1]])
            elif direction == "DOWN":
                newCoords.append([i[0], i[1] + self.dimension])

        if self.verifyPixels(newCoords):
            self.pieceCoords = newCoords
            self.placeCoords = self.pieceCoords[0]
            self.placePiece()
        else:
            print("Position disallowed")

    def placePiece(self):
        for i in self.pieceCoords:
            pygame.draw.rect(self.window, self.colour, (i[0], i[1], self.dimension, self.dimension))
            pygame.draw.rect(self.window, (100, 100, 100), (i[0], i[1], self.dimension, self.dimension), 2)


class Outline(Piece):
    def __init__(self):
        super.__init__()

